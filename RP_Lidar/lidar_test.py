from rplidar import RPLidar

def test():
    lidar = RPLidar('COM6')

    info = lidar.get_info()
    print(info)

    health = lidar.get_health()
    print(health)

    for i, scan in enumerate(lidar.iter_scans()):
        print('%d: Got %d measurments' % (i, len(scan)))
        if i > 10000:
            break

    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()


if __name__ == '__main__':
    test()
