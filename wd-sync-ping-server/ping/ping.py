# -*- coding: utf-8 -*-
import subprocess
import json
import requests
import time
from .conf import ip_lists, lost_info, base_url, token
from apscheduler.schedulers.blocking import BlockingScheduler


def ping_job():
    try:
        session = requests.Session()
        for ip_info in ip_lists:
            ip_addr = ip_info['ip']
            ip_isp = ip_info['isp']
            ip_location = ip_info['isp2']
            ping_res = subprocess.Popen(["ping", "-c2", "-w2", ip_addr], stdout=subprocess.PIPE).stdout.read()
            if lost_info in ping_res.decode('utf8'):
                avg_latency = "loss"
            else:
                latency = ping_res.decode('utf8').split('min/avg/max/mdev = ', 1)[1].split('/', 3)
                avg_latency = latency[1]
                unit = latency[3].split(' ')[1].split('\n')[0]
                avg_latency = avg_latency + unit

            wd_url = '{}/{}.json'.format(base_url, ip_isp)
            params = {'auth': token}
            data = {ip_location: avg_latency}
            headers = {"Connection": "keep-alive"}
            session.patch(wd_url, params=params, headers=headers, data=json.dumps(data))
            time.sleep(2)
        session.close()

    except Exception as e:
        print(e)
    return None


def daemon_ping_job():
    sched = BlockingScheduler()
    sched.add_job(ping_job, 'interval', seconds=60)
    sched.start()


if __name__ == '__main__':
    ping_job()
