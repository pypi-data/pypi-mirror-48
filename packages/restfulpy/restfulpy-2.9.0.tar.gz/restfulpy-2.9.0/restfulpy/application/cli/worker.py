import signal
import sys
import threading

from nanohttp import settings

from restfulpy.cli import Launcher, RequireSubCommand


class StartLauncher(Launcher):
    __command__ = 'start'

    @classmethod
    def create_parser(cls, subparsers):
        parser = subparsers.add_parser(
            cls.__command__,
            help='Starts the background worker.'
        )

        parser.add_argument(
            '-g',
            '--gap',
            type=int,
            default=None,
            help='Gap between run next task.'
        )

        parser.add_argument(
            '-s',
            '--status',
            default=[],
            action='append',
            help='Task status to process'
        )

        parser.add_argument(
            '-n',
            '--number-of-threads',
            type=int,
            default=None,
            help='Number of working threads'
        )
        return parser

    def launch(self):

        from restfulpy.taskqueue import worker

        signal.signal(signal.SIGINT, self.kill_signal_handler)
        signal.signal(signal.SIGTERM, self.kill_signal_handler)

        if not self.args.status:
            self.args.status = {'new'}

        if self.args.gap is not None:
            settings.worker.merge({'gap': self.args.gap})

        print(
            f'The following task types would be processed with gap of '
            f'{settings.worker.gap}s:'
        )
        print('Tracking task status(es): %s' % ','.join(self.args.status))

        number_of_threads = \
            self.args.number_of_threads or settings.worker.number_of_threads
        for i in range(number_of_threads):
            t = threading.Thread(
                    target=worker,
                    name='restfulpy-worker-thread-%s' % i,
                    daemon=True,
                    kwargs=dict(
                        statuses=self.args.status,
                        filters=self.args.filter
                    )
                )
            t.start()

        print('Worker started with %d threads' % number_of_threads)
        print('Press Ctrl+C to terminate worker')
        signal.pause()

    @staticmethod
    def kill_signal_handler(signal_number, frame):

        if signal_number == signal.SIGINT:
            print('You pressed Ctrl+C!')
        elif signal_number in (signal.SIGTERM, signal.SIGKILL):
            print('OS Killed Me!')

        sys.stdin.close()
        sys.stderr.close()
        sys.stdout.close()
        sys.exit(1)


class CleanupLauncher(Launcher):
    @classmethod
    def create_parser(cls, subparsers):
        return subparsers.add_parser(
            'cleanup',
            help='Clean database before starting worker processes'
        )

    def launch(self):
        from restfulpy.orm import DBSession
        from restfulpy.taskqueue import RestfulpyTask

        RestfulpyTask.cleanup(DBSession, filters=self.args.filter)
        DBSession.commit()


class WorkerLauncher(Launcher, RequireSubCommand):
    @classmethod
    def create_parser(cls, subparsers):
        parser = subparsers.add_parser(
            'worker',
            help="Task queue administration"
        )
        parser.add_argument(
            '-f',
            '--filter',
            default=None,
            type=str,
            action='store',
            help='Custom SQL filter for tasks'
        )

        worker_subparsers = parser.add_subparsers(
            title="worker command",
            dest="worker_command"
        )
        StartLauncher.register(worker_subparsers)
        CleanupLauncher.register(worker_subparsers)
        return parser
