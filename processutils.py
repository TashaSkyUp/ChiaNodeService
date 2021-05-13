import psutil
import sys
import datetime
import pathlib

def get_chia_pids():
    out = []
    for pid in psutil.pids():
        try:
            proc = psutil.Process(pid)
            with proc.oneshot():
                p_name = proc.name()
                if (("chia" == p_name) or ("chia.exe" == p_name)):
                    out += [pid]
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
        dirs = [tmp[0][2:], tmp[1][2:], tmp[2][2:]]
        out = []
        for dir in dirs:
            root_directory = pathlib.Path(dir)
            size = sum(f.stat().st_size for f in root_directory.glob('**/*') if
                       (f.is_file() &
                        ("gvfs" not in f.name))
            )
            out += [(dir, size)]

    return out


def get_chia_data(pid):
    dic = {'time': [], 'id': [], 'cur_cpu': [], 'tot_reads': [],
           'tot_writes': [], 'tot_read': [], 'tot_write': [],
           'cur_dir_size_1': [],
           'cur_dir_size_2': [],
           'cur_dir_size_3': []
           }
    dir_sizes = get_chia_dirs(pid)
    try:
        proc = psutil.Process(pid)
    except:
        raise

    with proc.oneshot():
        try:
            open_files = [ opf.path for opf in proc.open_files()]

            dic['time'] += [datetime.datetime.now()]
            dic['id'] +=  [open_files[0].split(".")[-2].split("_")[-1]]
            dic['cur_cpu'] += [proc.cpu_percent(.50)]
            dic['cur_dir_size_1'] += [dir_sizes[0][1]]
            dic['cur_dir_size_2'] += [dir_sizes[1][1]]
            dic['cur_dir_size_3'] += [dir_sizes[2][1]]
            dic['tot_reads'] += [proc.io_counters().read_count]
            dic['tot_writes'] += [proc.io_counters().write_count]
            dic['tot_read'] += [proc.io_counters().read_bytes]
            dic['tot_write'] += [proc.io_counters().write_bytes]

        except:
            print("Unexpected error:", sys.exc_info()[0])
            print(proc.open_files())
            raise
    return dic