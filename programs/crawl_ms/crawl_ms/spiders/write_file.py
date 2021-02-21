import json

with open("ms.json") as f:
    text = json.load(f)

# print(text["data"][0])

# rec = text["data"][0]["Recommendation"]
# exp = text["data"][0]["Comments"]
# link = text["data"][0]["Security Center"]

# line_1 = f"- [ ] **{rec}**"
# line_2 = f"  - *{exp}*"
# line_3 = f"  - [{link}]({link})"

# print(line_1)
# print(line_2)
# print(line_3)

# print(len(text["data"]))

for i in range(len(text["data"])):
    rec = text["data"][i]["Recommendation"]
    exp = text["data"][i]["Comments"]
    link = text["data"][i]["Security Center"]

    line_1 = f"- [ ] **{rec}**"
    line_2 = f"  - *{exp}*"
    line_3 = f"  - [{link}]({link})"
    with open("security_recs_checklist.md", "a+") as w:
        w.write(str(line_1))
        w.write("\n")
        w.write(str(line_2))
        w.write("\n")
        w.write(str(line_3))
        w.write("\n")

    # print(line_1)
    # print(line_2)
    # print(line_3)
    # print("")

# with open("security_recs_checklist.md", "a+") as w:
#     w.write(str(text))
