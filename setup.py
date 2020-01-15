#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('mp4 file --> frames...')
print()
get_ipython().system('ffmpeg -r 60 -i *.mp4 -vsync 0 -start_number 0 frame_%06d.jpg -hide_banner')
get_ipython().system('mkdir train')
get_ipython().system('mv frame_00* train')
print("store frames to '/train'")
print()

print("unzip file --> '/label'...")
print()
get_ipython().system('unzip *.zip -d label')
get_ipython().system('cp label/obj.names .')
get_ipython().system('rm label/obj.names')

txt = get_ipython().getoutput('ls label/')
jpg = get_ipython().getoutput('ls train/')

print("-")
classes = 0
print("reading obj.names...")
#print()
with open('obj.names') as fp:
    for cnt, line in enumerate(fp):
        print("- class {}: {}".format(cnt, line), end="")
        classes+=1

print()
print()
print('combining labels and images...')
#print()
get_ipython().system('cp label/* train/')

print("writing path to train.txt...")
#print()
p = get_ipython().getoutput('pwd')
p = p[0]
f = open("train.txt", "w")
for i in range(len(jpg)):
    f.write('{}/train/{}\n'.format(p, jpg[i]))
    #f.write('{}/train/{}\n'.format(p, txt[i]))
f.close()

print('set up train.data...')
#print()
f = open("train.data", "w")
f.write('classes = {}\n'.format(classes))
f.write('train = {}/train.txt\n'.format(p))
#valid  = /path/to/snowman/snowman_test.txt
f.write('names = {}/obj.names\n'.format(p))
f.write('backup = {}'.format('backup'))
f.close()

print('process completed!')
