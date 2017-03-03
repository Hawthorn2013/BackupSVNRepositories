import os
import socket
import datetime
import sys


def BackupSVNRepository(src_path, des_path):
    if not os.path.isdir(src_path):
        print('Error: %s is not exist.' % src_path)
        return
    if not os.path.isdir(des_path):
        print('Error: %s is not exist.' % des_path)
        return
    repository_name = os.path.split(src_path)[1]
    computer_name = socket.gethostname()
    dump_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    src_path_abs = os.path.abspath(src_path)
    des_file_name = format('%s_%s_%s.svndump' % (repository_name, computer_name, dump_time))
    des_file_abs = os.path.abspath(os.path.join(des_path, des_file_name))
    backup_cmd = format('svnadmin dump %s 1> %s' % (src_path_abs, des_file_abs))
    log_time = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    log_start = format('Dump %s Start' % repository_name)
    log_stop = format('Dump %s Stop' % repository_name)
    print(log_time)
    print(log_start)
    print(backup_cmd)
    os.system(backup_cmd)
    print(log_stop)


def BackupSVNRepositories(src_path, des_path):
    if not os.path.isdir(src_path):
        print('Error: %s is not exist.' % src_path)
        return
    if not os.path.isdir(des_path):
        print('Error: %s is not exist.' % des_path)
        return
    rep_list = os.listdir(src_path)
    for rep in rep_list:
        if not os.path.isdir(os.path.join(src_path, rep)):
            continue
        BackupSVNRepository(os.path.join(src_path, rep), des_path)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Error: Must have 2 parameters.')
        print('Usage: %s SrcDir DstDir' % sys.argv[0])
        exit(1)
    BackupSVNRepositories(sys.argv[1], sys.argv[2])
    exit(0)