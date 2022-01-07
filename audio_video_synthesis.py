# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 09:24
# @Author  : Kenny Zhou
# @FileName: audio_video_synthesis.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

import ffmpeg
import argparse
from pathlib import Path

def synthesis_V_A(v,a,output):

	input_video = ffmpeg.input(v)
	input_audio = ffmpeg.input(a)

	ffmpeg.concat(input_video, input_audio, v=1, a=1).output(output,  vcodec='libx264').run()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='将分离的音视频文件合并.')
	# nargs='+' 获取多个参数组合为列表
	parser.add_argument('-v', type=str,metavar='file',
											help='视频路径')
	parser.add_argument('-a', type=str,metavar='file',
											help='音频路径')
	parser.add_argument('-o', type=str,metavar='file',
											help='输出路径')
	parser.add_argument('-auto', action='store_true',
											help='自动处理文件名,如果存在-o则强制使用-o')

	args = parser.parse_args()

	if args.v != None:
		args.v = Path(args.v)
	if args.a != None:
		args.a = Path(args.a)

	if args.v != None and args.a != None:
		if args.o is None and args.auto is None:
			print("输出路径不能为空！")
			exit(1)
		else:
			if not args.auto:
				synthesis_V_A(v=args.v,a=args.a,output=args.o)
			else:
				if args.o is None:
					#自动重命名
					synthesis_V_A(v=args.v, a=args.a, output=args.v.rename(args.v.stem+".mp4"))
				else:
					# 如果存在-o则强制使用-o
					synthesis_V_A(v=args.v, a=args.a, output=args.o)
			print(f"已经输出到{str(args.o)}")
	parser.print_help()
	exit(0)