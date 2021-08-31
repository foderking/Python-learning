import os
import pprint
import sys, time


start = time.time()
unerror = {}
dat = []
empty = []
none = ('folder.jpg', 'ope')
file = open('C:\\Users\\Foderking\\Downloads\\Without_Lyric_File.txt', 'w')
os.chdir("C:\\Foderking\\SMLoadr-win-x64_v1.9.5\\DOWNLOADS")


def main() : 
    # shows all artists
    ar_ = os.listdir()
    ar_dir = os.getcwd()

    for artist in ar_ :
        # changes dir to artist
        ar_path = os.path.join( ar_dir, artist)
        os.chdir(ar_path)
        # show all albums
        al_ = os.listdir()
        al_dir = os.getcwd()

        for album in al_ :
            # changes dir to album
            al_path = os.path.join(al_dir, album)
            if os.path.isdir(al_path) :
                os.chdir(al_path)
                # shows all current songs or discs
                so_ = os.listdir()
                so_dir = os.getcwd()
                n_lyric()
                try :
                    if os.path.isdir(os.path.abspath(so_[0])) :
                        for disc in so_ :
                            #changes dir to disc
                            di_path = os.path.join(so_dir, disc)
                            if os.path.isdir(di_path) : 
                                os.chdir(di_path)
                                n_lyric()
                            else : 
                                pass
                except IndexError :
                    pass            

                else :
                    pass
            else : 
                pass

def al_m():
    """
  *  check if the directory contains folders
 *   if so go through all folders and do step 1
*    else call the n_lyric function
    """
    # get path info ... 
    dirs = os.listdir()
    path = os.getcwd()  
    # Check if directory contains folders
    if len(dirs) == 0:
        empty.append(os.path.abspath(path))
    elif os.path.isdir(dirs[0])  :
        # go through all folder and do step 1
        try :
            for sub in dirs:
                if  sub in none :
                    continue
                # elif sub == 'Friday Night Lights (Album)':
                #     print('jjjjjjjjjjjjjjjjjj')
                os.chdir(os.path.abspath(sub))
                al_m()
                os.chdir('..\\')
        except NotADirectoryError:
            dat.append(os.path.abspath(sub))
    else:
        n_lyric()
        pass

            
def n_lyric(a):
    os.chdir(os.path.abspath(a))
    ly = []
    mp3 = []
    all_ = os.listdir()

    for i in all_ :
        if i.endswith('.lrc') or i.endswith('.txt'):
            ly += [i[:-4]]
        elif i.endswith('.mp3') :
            mp3 += [i[:-4]]
    n_with_ly  = set(mp3) - set(ly)

    for i in n_with_ly :
        try:
            file.write(os.path.abspath(i))
            file.write('\n')
        except UnicodeEncodeError :
            unerror[i] = os.path.abspath(i)
    if n_with_ly :
        print(n_with_ly)
        print()

    else : 
        pass
    
def walk():
    for folder, sub_f, fil in os.walk('C:\\Foderking\\SMLoadr-win-x64_v1.9.5\\DOWNLOADS'):
        if fil != []:
            n_lyric(folder)

# al_m()
walk()
# main()
# os.chdir('C:\\Foderking\\SMLoadr-win-x64_v1.9.5\\DOWNLOADS\\J. Cole\\Friday Night Lights (Album)')
# n_lyric()
print(f'Finished in {time.time() - start}s')
# file.close()

# print(dat)