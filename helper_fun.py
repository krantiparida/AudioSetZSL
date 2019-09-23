# This code is for reading features (video, audio) from the h5 files using python3
# h5 files contains the features extracted from the pre-trained network and the youtube-id.
# h5 contains keys ['data', 'video_urls'] 

import h5py
import argparse
import os
import time

def read_features(path):
    hf = h5py.File(path, 'r')
    # keys = list(hf.keys())
    data = hf['data']
    url = [str(u,'utf-8') for u in list(hf['video_urls'])]

    return data, url

def download_video(label, out_folder, inp_folder):
	print('Downloading for class:{}'.format(label))
	
	if not os.path.exists(os.path.join(out_folder, label)):
		os.mkdir(os.path.join(out_folder,label))
	
	if not os.path.exists(os.path.join(out_folder, 'problem_vids')):
		os.mkdir(os.path.join(out_folder, 'problem_vids'))

	f = open(os.path.join(out_folder, 'problem_vids', label+'.txt'), "w")
	f.close()
	out_file = os.path.join(out_folder, label, 'temp'+'.%'+'(ext)s')
	with open(os.path.join(inp_folder, label, 'full_labels.txt')) as txtfile:
		num_lines = sum(1 for line in open(os.path.join(inp_folder, label, 'full_labels.txt')))
		vids = 1
		for lines in txtfile.readlines():
			linesPart = lines.split(', ')
			url = ' https://www.youtube.com/watch?v='+linesPart[1]
			
			print('-------------Downloading:{}/{}----------------'.format(vids, num_lines))
			start_time = time.time()

			cmd = 'youtube-dl --quiet --no-warnings -f ' + '\'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best\''+' -o '+'\''+out_file+'\''+' '+url
			# print(cmd)
			download = os.system(cmd)
			if download != 0:
				f = open(os.path.join(out_folder,'problem_vids',label+'.txt'), "a")
				f.write(", ".join(linesPart))
				f.close()
			else:
				os.system('ffmpeg -nostats -loglevel 0 -i '+os.path.join(out_folder,label)+'/temp.mp4 -ss '+linesPart[2]+' -strict -2 -t '+str(
				    float(linesPart[3])-float(linesPart[2]))+' '+os.path.join(out_folder, label)+'/'+str("%03d" % (vids,))+'.mp4')
				os.remove(os.path.join(out_folder, label, 'temp.mp4'))
			vids += 1
			print('Time Taken in Seconds:{}'.format(time.time() - start_time))
			exit()


