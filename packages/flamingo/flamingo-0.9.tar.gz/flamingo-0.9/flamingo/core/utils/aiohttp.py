import os

from aiohttp.web import StaticResource


class DirectoryExporter:
    def __init__(self, path, prefix=''):
        self.path = path
        self.prefix = prefix
        self.resource = StaticResource('', path, show_index=True,
                                       follow_symlinks=True)
        self.show_index = True

    async def __call__(self, request):
        path = request.path

        # remove prefix
        if self.prefix:
            path = os.path.join(
                '/', os.path.relpath(request.path, self.prefix))

        # directory listing
        if self.show_index:
            test_path = os.path.join(self.path, path[1:])

            # serve index.html if present
            if os.path.isdir(test_path):
                test_path = os.path.join(test_path, 'index.html')

                if os.path.exists(test_path):
                    path = os.path.join(path, 'index.html')

        # run static resource
        request.match_info['filename'] = path[1:]
        response = await self.resource._handle(request)

        # disable caching
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # NOQA

        return response
