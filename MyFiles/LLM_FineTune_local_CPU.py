# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 15:34:17 2025
jsoon transformers peft datasets PyTorch .etc
@author: SUISJ1999
"""
#第一步：测试一下微调之前的模型是否可用
"""
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
model_name = "/Learn/2025/LLM/deepseekr1-1.5b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
#tokenizer = AutoTokenizer.from_pretrained(model_name).to("cuba") #缓存进显存
print("模型加载成功")
"""

#测试训练前模型

"""
model = AutoModelForCausalLM.from_pretrained(model_name)

from transformers import pipeline
pipe = pipeline(task="text-generation", model =model,tokenizer=tokenizer)
prompt = "请证明根号2是一个无理数"
#prompt = input()

#添加一个对话模板，给AI参考, 多行str

prompt_style_chat = "请写出一个恰当的回答来完成当前对话任务。

### Instruction:
你是一名助人为乐的助手。

### Question:
{}

### Response:
<think>{}"

#generated_texts = pipe(prompt, max_length=512,truncation=True,num_return_sequences=1)  #不使用对话模板
generated_texts = pipe(prompt_style_chat.format(prompt, ""), max_length=512,truncation=True,num_return_sequences=1)  #使用对话模板
print("开始回答：", generated_texts[0]["generated_text"])
"""

"""     引入对话模板的思路源泉
model = AutoModelForCausalLM.from_pretrained(model_name)
prompt="天空为什么是蓝的？"

inputs = tokenizer([prompt_style_chat.format(prompt, "")], return_tensors="pt") #使用对话模板。
#inputs = tokenizer([prompt], return_tensors="pt")  #不使用对话模板，出现乱对话，因为max_new_tokens?
#print(inputs)
outputs = model.generate(
    input_ids=inputs.input_ids,
    max_new_tokens=512,
    use_cache=True
) #输入为序列，输出亦为序列
response = tokenizer.batch_decode(outputs)  #将索引转化为文字
print(response[0])
"""


#第二步：制作数据集
"""
import json
from data_prepare import samples
with open("datasets.jsonal","w",encoding="utf-8") as f:
    for s in samples:
        json_line = json.dumps(s,ensure_ascii=False)
        f.write(json_line + "\n")
    else:
        print("data prapared")
"""



#第三步：准备训练集和测试集
"""
from datasets import load_dataset
dataset = load_dataset(path="json",data_files={"train":"datasets.jsonal"},split="train")
train_test_split = dataset.train_test_split(test_size=0.1)  #1：9 测训比
train_dataset=train_test_split["train"]
eval_dataset = train_test_split["test"]
print("完成数据准备工作")
print(train_dataset[0])
"""



#第四步：编写tokennizer处理工具
"""
def tokenizer_function(many_samples):  #many_samples
    texts = [f"{prompt}\n{completion}" for prompt,completion in 
             zip(many_samples["prompt"],many_samples["completion"])]
    tokens = tokenizer(texts,truncation=True,max_length = 512, padding="max_length")
    tokens["labels"]=tokens["input_ids"].copy()
    
    return tokens

tokenized_train_dataset =train_dataset.map(tokenizer_function,batched=True) #转化为序列，方便微调
tokenized_eval_dataset = eval_dataset.map(tokenizer_function,batched=True)  #转化为序列，方便微调

print("完成数据tokenizing")
print(tokenized_train_dataset[0])
"""


# 第五步：量化设置

"""
#from transformers import  AutoModelForCausalLM  #代码分模块使用时，一定要取消本行注释
#from transformers import BitsAndBytesConfig  #该模块需要用到GPU
#quantization_config = BitsAndBytesConfig(load_in_8bit=True)#必须有GPU
#model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config= quantization_config, device_map="auto")
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")   #device_map="auto"，数据会传输到 cpu 和 disk  后续trainer会报错
print("完成量化模型的加载")
"""


#第六步：lora微调设置

"""
from peft import get_peft_model,LoraConfig,TaskType

lora_config=LoraConfig(
    r=8, lora_alpha=16,lora_dropout=0.05,task_type=TaskType.CAUSAL_LM
    )
model = get_peft_model(model,lora_config)
model.print_trainable_parameters()
print("lora微调设置完毕")
"""

#第七步：设置训练参数并进行训练
"""
from transformers import TrainingArguments,Trainer

training_args= TrainingArguments(
    output_dir="./finetuned_models",
    num_train_epochs=2,  #训练轮次，视硬件而定
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    fp16=True,
    logging_steps=10,
    save_steps=100,
    eval_strategy="steps",
    eval_steps=10,
    learning_rate=3e-5,
    logging_dir="./logs",
    run_name="deepseek-r1-distill-finetune"
    )
print("训练参数设置完毕")



trainer = Trainer(
    model=model,#lore的模型
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset =tokenized_eval_dataset,
    
    ) #定义训练器

print("开始训练") #10个样本？
trainer.train()
print("训练完成")
"""

#第八步：先保存lora模型，再保存全量模型

"""
save_path="./saved_model"
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
print("Lora模型已保存")

final_save_path="./final_saved_path"
from peft import PeftModel
base_model=AutoModelForCausalLM.from_pretrained(model_name) #微调前模型
model =PeftModel.from_pretrained(base_model, save_path)  #save_path= lora模型
model = model.merge_and_unload()
model.save_pretrained(final_save_path)
tokenizer.save_pretrained(final_save_path)
print("全量模型已保存")
"""

#第九步：测试训练后模型
"""
from transformers import AutoTokenizer
from transformers import  AutoModelForCausalLM
final_save_path="./final_saved_path"
model = AutoModelForCausalLM.from_pretrained(final_save_path)
tokenizer = AutoTokenizer.from_pretrained(final_save_path)
#tokenizer = AutoTokenizer.from_pretrained(model_name).to("cuba") #缓存进显存
print("模型加载成功")

from transformers import pipeline
pipe = pipeline(task="text-generation", model =model,tokenizer=tokenizer)
prompt = "why the sky is blue?"
#prompt = input()

generated_texts = pipe(prompt, max_length=512,truncation=True,num_return_sequences=1)
print("开始回答：", generated_texts[0]["generated_text"])
"""