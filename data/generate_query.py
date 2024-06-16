import json
import argparse
from tqdm import tqdm
from volcenginesdkarkruntime import Ark

def process_file(input_file, output_file):
    data = json.load(open(input_file, 'r'))

    output_conversations = []

    prompt = "对于接下来给定的文字，我希望你能猜测出它的问题是什么(最好有针对性一些），并直接回复问题本身(字数在10字以上)，不需要其他的话语，以下是具体的文字。\n---\n"

    # build doubao client
    client = Ark(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
    )

    # Non-streaming:
    print("----- standard request -----")
    system_ = "作为一位专业的旅游顾问，你的任务是提供详尽、实用的旅行建议。请确保你的回答包括目的地的特色景点、交通指南、住宿推荐、当地美食和文化体验。以轻松、友好的语气分享你的知识，让读者仿佛身临其境。建议基于实际经验和可靠来源，为各种类型的旅行者提供个性化的旅行方案。"

    for item in tqdm(data, desc=''):
        content = prompt + item['conversation'][0]['output']
        completion = client.chat.completions.create(
            model="ep-20240612143744-wn9zh",
            messages=[
                {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
                {"role": "user", "content": content},
            ],
        )
        result = completion.choices[0].message.content

        conversation_entry = {
            'system': system_,
            'input': result,
            'output': item['conversation'][0]['output']
        }
        output_conversations.append({"conversation": [conversation_entry]})

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_conversations, f, ensure_ascii=False, indent=4)

    print(" 0_o $-$ ")

def main():
    parser = argparse.ArgumentParser(description="Process an input JSON file and produce an output JSON file.")
    parser.add_argument('input_file', type=str, help="Input JSON file")
    parser.add_argument('output_file', type=str, help="Output JSON file")

    args = parser.parse_args()

    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    # usage: python process_conversations.py result.json _one_epoch_chat.json
    main()