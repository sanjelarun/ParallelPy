import  subprocess

batcmd = "pytest /home/hduser/PycharmProjects/ParallelPy/result/gen.py"
dir = 'pytest /home/hduser/PycharmProjects/ParallelPy/result/knn_gen.py -W ignore::DeprecationWarning'

process= subprocess.run(dir, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# st, er = process.communicate()
print(process.stdout)
print(process.stderr)