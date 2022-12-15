import argparse

def args_reader():
    parser = argparse.ArgumentParser(description='Process some paths.')

    parser.add_argument (
        "--in",
        dest='resource',
        default="../resource",
        help="Папка, в которой хранятся словари.",
        type=str
    )

    parser.add_argument(
        "--out",
        dest='pathout',
        default="/tmp/streaming/in",
        help="Папка с результирующими данными.",
        type=str
    )

    parser.add_argument(
        "--duration",
        dest='duration',
        default=60,
        help="Streaming duration in seconds.",
        type=int
    )

    """
    * Wait time between two batches of records, in seconds, with an element
    * of variability. If you say 10 seconds, the system will wait between 5s
    * and 15s, if you say 20s, the system will wait between 10s and 30s, and
    * so on.
    """
    parser.add_argument(
        "--waitTime",
        dest='wait_time',
        default=5,
        help="Wait time between two batches of records, in seconds, with an element of variability.",
        type=int
    )


    return parser.parse_args()

if __name__ == '__main__':
    args = args_reader()
    print("resource = {0}".format(args.resource))
    print("pathout = {0}".format(args.pathout))

    print("duration = {0}".format(args.duration))
    print("batch_size = {0}".format(args.batch_size))
    print("wait_time = {0}".format(args.wait_time))
