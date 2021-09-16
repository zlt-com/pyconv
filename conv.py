#!/usr/bin/env python

import sys
import getopt
import os

class ConvImg:
    def getFileList(self,dir, Filelist, ext=None):
        """
        获取文件夹及其子文件夹中文件列表
        输入 dir：文件夹根目录
        输入 ext: 扩展名
        返回： 文件路径列表
        """
        newDir = dir
        if os.path.isfile(dir):
            if ext is None:
                Filelist.append(dir)
            else:
                if ext in dir[-3:]:
                    Filelist.append(dir)

        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                newDir = os.path.join(dir, s)
                self.getFileList(newDir, Filelist, ext)

        return Filelist

    def main(self,argv):
        try:
            opts, args = getopt.getopt(argv, "hi:o:f:", ["ifile=", "ofile="])
            # print(opts, args)
        except getopt.GetoptError:
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        try:
            cmds = []
            for opt, arg in opts:
                if opt == '-h':
                    print('test.py -i <inputfile> -o <outputfile>')
                    sys.exit()
                elif opt in ("-i", "--ifile"):
                    inputfile = arg
                elif opt in ("-o", "--ofile"):
                    outputfile = arg
                elif opt in ("-f", "--ftype"):
                    file_name = os.path.splitext(args[0])
                    cmd = ''
                    if arg == "pdf":
                        if len(args) == 1:
                            cmd = 'unoconv -f pdf  {0} {1}'.format(args[0], '')
                            cmds.append(cmd)
                        else:
                            print("args error.")
                    elif arg == 'img':
                        cmd = 'unoconv -f pdf  {0} {1} '.format(args[0], '')
                        # cmd2 = 'convert ' + \
                        #     file_name[0]+'.pdf -append -flatten ' + \
                        #     file_name[0]+'.jpg'
                        cmd2 = 'gs -dSAFER -dBATCH -dNOPAUSE -r250 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sDEVICE=jpeg -sOutputFile=%d.jpg '+file_name[0] +'.pdf'
                        cmds.append(cmd)
                        cmds.append(cmd2)
            for c in cmds:
                # pass
                os.system(c)
            imgs = self.getFileList(".", [], "jpg")
            imgs = sorted(imgs)
            cmd3 = 'convert -append ' + ' '.join(imgs) + ' ' + file_name[0]+".jpg"
            os.system(cmd3)
            for im in imgs:
                pass
                # os.remove(im)
        except Exception as e:
            print(e)
            sys.exit(2)

    def toImage(self,file_path):
        try:
            (filepath,tempfilename) = os.path.split(file_path)
            cmds = []
            file_name = os.path.splitext(tempfilename)
            cmd = ''
            cmd = 'unoconv -f pdf  {0} {1} '.format(file_path, '')
            cmd2 = 'cd '+filepath+' && gs -dSAFER -dBATCH -dNOPAUSE -r250 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sDEVICE=jpeg -sOutputFile=%d.jpg '+filepath+'/'+file_name[0] +'.pdf'
            print(cmd,cmd2)
            cmds.append(cmd)
            cmds.append(cmd2)
            for c in cmds:
                # pass
                os.system(c)
            imgs = self.getFileList(filepath, [], "jpg")
            imgs = sorted(imgs)
            cmd3 = 'cd '+filepath+' && convert -append ' + ' '.join(imgs)+' '+file_name[0]+".jpg"
            print(cmd3)
            os.system(cmd3)
        except Exception as e:
            return e
        finally:
            return "转换完成"

# if __name__ == "__main__":
#     main(sys.argv[1:])
