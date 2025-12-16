
print("ejecutanto: ", __file__)

from loaders.file_loader import load_logs

df = load_logs("fortigate_logs_sample.csv")

print(df.head())