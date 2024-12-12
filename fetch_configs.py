import requests

# لینک‌های کانفیگ
urls = [
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/EternityAir.txt",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt"
]

# فایل خروجی
output_file = "merged_configs.txt"

def fetch_configs(urls):
    configs = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                configs.append(response.text.strip())
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return configs

def save_to_file(configs, output_file):
    with open(output_file, 'w') as file:
        file.write("\n".join(configs))

if __name__ == "__main__":
    configs = fetch_configs(urls)
    save_to_file(configs, output_file)
    print(f"Configs saved to {output_file}")
