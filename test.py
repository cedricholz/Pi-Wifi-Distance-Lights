import Utils as utils

x = utils.file_to_json("listener_data.json")

utils.json_to_file(x, "test.json")

print(5)