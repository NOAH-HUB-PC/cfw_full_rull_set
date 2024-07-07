import requests
import re

from rule_url_gen import rule_url_gen

url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/README.md'
rm = requests.get(url)
rm_content = rm.content.decode("utf-8", "ignore")
rm_blocks = rm_content.split("\n\n\n")
rm_blocks = rm_blocks[1:]
group_set = set()
with open("blackmatrix7_full_rule_set.ini", "w", encoding='utf-8') as ini_w:
    ini_w.writelines("[custom]\n")
    for item in rm_blocks:
        if "Clash/Direct" in item:
            item_blocks = item.replace("\n", "").replace(" ", "").split("|")
            for each_rule in item_blocks:
                if "Direct" in each_rule:
                    group_set.add("Direct")
                    rule_set_content = rule_url_gen("Direct", each_rule)
                    ini_w.writelines(rule_set_content)
        else:
            item_blocks = item.replace("\n", "").replace(" ", "").split("|")
            class_name = item_blocks[1]
            for each_rule in item_blocks:
                if "blackmatrix7" in each_rule:
                    group_set.add(class_name)
                    rule_set_content = rule_url_gen(class_name, each_rule)
                    ini_w.writelines(rule_set_content)
    ini_w.writelines("ruleset=Direct,[]GEOIP,CN\n")
    ini_w.writelines("ruleset=🐟漏网之鱼,[]FINAL\n")
    group_set.add("🐟漏网之鱼")
    pass
    ini_w.writelines("custom_proxy_group=🚀节点选择`select`[]♻️自动选择`[]🚀手动切换`[]DIRECT\n")
    ini_w.writelines("custom_proxy_group=🚀手动切换`select`.*\n")
    ini_w.writelines("custom_proxy_group=♻️自动选择`url-test`.*`http://www.gstatic.com/generate_204`300,,50\n")
    for it in group_set:
        ini_w.writelines("custom_proxy_group="+it+"`select`[]🚀节点选择`[]♻️自动选择`[]🚀手动切换`[]DIRECT\n")
    ini_w.writelines("enable_rule_generator=true\n")
    ini_w.writelines("overwrite_original_rules=true\n")

