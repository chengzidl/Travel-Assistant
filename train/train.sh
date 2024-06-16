FINETUNE_CFG="internlm2_chat_7b_qlora_alpaca_e3.py"
LLM="internLm2-chat-7b"
# config
PTH_PATH="work_dir/xxx" 
hf_SAVE_PATH=""
LLM_ADAPTER=""
SAVE_PATH=""


xtuner train ${FINETUNE_CFG} --deepspeed deepspeed_zero1
xtuner convert pth_to_hf ${FINETUNE_CFG} ${PTH_PATH} ${hf_SAVE_PATH}
xtuner convert merge ${LLM} ${LLM_ADAPTER} ${SAVE_PATH}