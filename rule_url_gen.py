import re


def rule_url_gen(class_name, each_rule):
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    rule_url_list = re.findall(p1, each_rule)
    if len(rule_url_list) > 1:
        for it in rule_url_list:
            if "blackmatrix7" in it:
                rule_url = it
    else:
        rule_url=rule_url_list[0]
    list_name = rule_url.split("/")
    list_name = list_name[-1] + ".list"
    rule_set_content = "ruleset=" + class_name + "," + rule_url + "/" + list_name + "\n"
    return rule_set_content
