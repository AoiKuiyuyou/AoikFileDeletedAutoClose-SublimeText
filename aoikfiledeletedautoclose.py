#
import os
import os.path

import sublime
import sublime_plugin


#
_PACKAGE_NAME = 'AoikFileDeletedAutoClose'


#
class AoikFileDeletedAutoCloseEventListener(sublime_plugin.EventListener):

    # Called each time a view gets focus
    def on_activated(self, view):
        #
        settings = sublime.load_settings(
            '{0}.sublime-settings'.format(_PACKAGE_NAME))

        #
        plugin_is_enabled = settings.get('enable', True)

        if not plugin_is_enabled:
            return

        #
        debug_on = settings.get('debug', False)

        def print_func(text):
            if debug_on:
                print(text)

        #
        ignore_dirty_view = settings.get('ignore_dirty_view', True)

        # Get file path
        file_path = view.file_name()
        # ^ Can be None, which means no view is open.

        # If has a view and its file path not exists
        if file_path and (not os.path.exists(file_path)):
            #
            if ignore_dirty_view:
                #
                if view.is_dirty():
                    #
                    print_func(
                        '# {0}\nIgnore: {1}'.format(_PACKAGE_NAME, file_path))

                    #
                    return

            # Normalize the paths
            sublime_packages_normpath = \
                os.path.normpath(os.path.abspath(sublime.packages_path()))

            file_dir_normpath = \
                os.path.normpath(os.path.dirname(os.path.abspath(file_path)))

            # If the file path is under SublimeText's "Packages" directory,
            # ignore. This is because packages zipped into ".sublime-package"
            # files will open their settings files in a view with a fake file
            # path under the "Packages/User/" directory. We do not want to
            # close these views.
            if ((file_dir_normpath.replace('\\', '/') + '/')
                    .startswith(
                        sublime_packages_normpath.replace('\\', '/') + '/')):
                # ^ Add a trailing '/' to prevent situations like:
                # ^ 'Packages123'.startswith('Packages')

                #
                print_func(
                    '# {0}\nIgnore: {1}'.format(_PACKAGE_NAME, file_path))

                #
                return
            #
            else:
                # Set to scratch.
                # Scratch views never report as being dirty.
                view.set_scratch(True)

                # Define a callback to close the file
                def callback(view=view):
                    #
                    if view is not None:
                        # ^ "if view:" does not work in Sublime Text 2.0.2

                        #
                        window = view.window()

                        if window is not None:
                            #
                            window.run_command('close_file')

                            #
                            print_func(
                                '# {0}\nClose: {1}'.format(
                                    _PACKAGE_NAME, file_path
                                )
                            )

                # Register the callback
                sublime.set_timeout(callback, 0)

                #
                return
