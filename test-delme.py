import subprocess
cmd = "MediaInfo --Output=Video;%Duration% E:\\vegas-export\\future-projects\\[76]wavy-piano-drama-music\\cacat.m4v"
print(cmd)
result = subprocess.getoutput([cmd])
print(result)
