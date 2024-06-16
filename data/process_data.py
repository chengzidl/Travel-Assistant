import json
import argparse

def process_files(file, output_file):
    # read data
    json_data = json.load(open(file, 'r'))
    data = []

    # process file
    for item in json_data:
        newitem = {}
        newitem['system'] = "你现在对于中国各地的旅游攻略都很熟悉。"
        newitem['input'] = item['tag_list']
        newitem['output'] = item['desc']
        conve = {}
        conve['conversation'] = [newitem]
        data.append(conve)
    

    # output data to result.json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Processed {len(data)} items.")

def main():
    parser = argparse.ArgumentParser(description="Process two json files and combine their content into one.")
    parser.add_argument('file', type=str, help="input JSON file")
    parser.add_argument('output', type=str, help="Output JSON file")

    args = parser.parse_args()

    process_files(args.file, args.output)

if __name__ == "__main__":
    # usage: python process_json.py 9_search_contents_2024-06-09.json result.json
    main()