import psutil
import sys
import datetime
import pathlib
import re
def get_chia_pids():
    out = {}
    for pid in psutil.pids():
        try:
            proc = psutil.Process(pid)
            with proc.oneshot():
                p_name = proc.name()
                if ( ("chia" == p_name) or ("chia.exe" == p_name) ):
                    if len(proc.children()) == 0:
                        #if proc.
                        out[proc.ppid()] = proc.pid
        except (psutil.NoSuchProcess):
            pass


    return out

def get_chia_dirs(pid):
    try:
        proc = psutil.Process(pid)
    except:
        raise

    with proc.oneshot():
        tmp = proc.cmdline()[5:8]
        #print ("cmdline",proc.cmdline())
        #print (tmp)
        dirs=[]
        for part in proc.cmdline():
            if "/" in part:
                dirs+=[part]

        dirs = dirs[1:]

        #print(dirs)
        out = []
        for dir in dirs:
            #print(dir)
            root_directory = pathlib.Path(dir)
            files = root_directory.glob('**/*')
            fnames = [f.name for f in files]
            #print (fnames)

            files = root_directory.glob('**/*')
            fsizes = [f.stat().st_size for f in files]
            #flist = [f.stat().st_size for f in root_directory.glob('**/*') if ((f.is_file() & (not f.is_mount())))]
            print (fsizes)
            size = sum(fsizes)

            out += [(dir, size)]

    return out

def get_chia_plot_id(proc):

    logfile = proc.open_files()[0]
    if "path" in logfile.__dir__():
        logfile = logfile.path
        with open(logfile, "r") as log:
            header = log.readlines(1024)

        for s in header:
            if s[:4] == "ID: ":
                return s[4:]
    else:
        return "unknown"

def get_chia_data(pid):
    dic={}
    dir_sizes = get_chia_dirs(pid[0])

    try:
        proc = psutil.Process(pid[1])
    except:
        raise

    with proc.oneshot():
        try:
            print(proc.exe())
            open_files = [ opf.path for opf in proc.open_files()]
            children = proc.children()

            if len(children) > 0:
                return
                cmd = " ".join(proc.cmdline())
                dic["lane"] = cmd[cmd.index("/plot") + 5]

                #dic['id'] = "unknown"
                #logfile = children[0]
            else:
                cmd = " ".join(proc.cmdline())
                dic["lane"]=re.findall("plot\d+", cmd)[0][4:]
                dic['id'] = get_chia_plot_id(proc)

            dic['time'] = datetime.datetime.now()



            dic['cur_cpu'] = proc.cpu_percent(.50)
            dic['cur_dir_size_1'] = dir_sizes[0][1]
            dic['cur_dir_size_2'] = dir_sizes[1][1]
            if len(dir_sizes) >2:
                dic['cur_dir_size_3'] = dir_sizes[2][1]
            dic['tot_reads'] = proc.io_counters().read_count
            dic['tot_writes'] = proc.io_counters().write_count
            dic['tot_read'] = proc.io_counters().read_bytes
            dic['tot_write'] = proc.io_counters().write_bytes
            dic['start_time'] = proc.create_time()
            dic['io'] = proc.io_counters().write_bytes
            #dic['ionice'] = proc.ionice()

        except:
            print("Unexpected error:", sys.exc_info()[0])
            #print(proc.open_files())
            raise
    return dic