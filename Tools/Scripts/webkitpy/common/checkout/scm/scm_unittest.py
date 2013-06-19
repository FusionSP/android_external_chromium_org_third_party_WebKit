import unittest2 as unittest
from webkitpy.common.system.filesystem_mock import MockFileSystem

class SVNTestRepository(object):
        self.assertNotEqual(input_process.poll(), 0)
        self.assertItemsEqual(self.scm.changed_files(), ["test_file"])
        self.assertItemsEqual(self.scm.changed_files(), ["test_dir/test_file3", "test_file"])
        self.assertItemsEqual(self.scm.changed_files(), ["test_dir/test_file3", "test_file"])
        self.assertItemsEqual(self.scm.added_files(), [])
        self.assertItemsEqual(added_files, ["added_dir/added_file2", "added_file", "added_file3", "added_file4"])
        # Test also to make sure discard_working_directory_changes removes added files
        self.scm.discard_working_directory_changes()
        self.assertItemsEqual(self.scm.added_files(), [])
        self.assertItemsEqual(changed_files, ["test_dir/test_file3", "test_file"])
        self.assertItemsEqual(self.scm.changed_files_for_revision(4), ["test_file", "test_file2"])  # Git and SVN return different orders.
        self.assertItemsEqual(self.scm.changed_files_for_revision(2), ["test_file"])
        self.assertItemsEqual(self.scm.revisions_changing_file("test_file"), [5, 4, 3, 2])
        self.assertRegexpMatches(r3_patch, 'test3')
        self.assertNotRegexpMatches(r3_patch, 'test4')
        self.assertRegexpMatches(r3_patch, 'test2')
        self.assertRegexpMatches(self.scm.diff_for_revision(3), 'test2')
        self.assertIn('fizzbuzz7.gif', self.scm.changed_files())
        self.assertIn('fizzbuzz7.gif', self.scm.changed_files())
        self.assertNotIn('fizzbuzz7.gif', self.scm.changed_files())
        self.assertIn("added_dir/added_file", self.scm.added_files())
        self.assertIn("added_dir/added_file", self.scm.added_files())
        self.assertNotIn("added_dir", self.scm.added_files())
        self.assertIn("added_dir/added_file", self.scm.added_files())
        self.assertIn("added_dir/another_added_file", self.scm.added_files())
        self.assertIn("added_dir/another_added_file", self.scm.added_files())
    def _shared_test_move(self):
        write_into_file_at_path('added_file', 'new stuff')
        self.scm.add('added_file')
        self.scm.move('added_file', 'moved_file')
        self.assertIn('moved_file', self.scm.added_files())

    def _shared_test_move_recursive(self):
        os.mkdir("added_dir")
        write_into_file_at_path('added_dir/added_file', 'new stuff')
        write_into_file_at_path('added_dir/another_added_file', 'more new stuff')
        self.scm.add('added_dir')
        self.scm.move('added_dir', 'moved_dir')
        self.assertIn('moved_dir/added_file', self.scm.added_files())
        self.assertIn('moved_dir/another_added_file', self.scm.added_files())

        self.assertEqual(read_from_path('ChangeLog'), expected_changelog_contents)
        self.assertEqual(read_from_path('ChangeLog'), expected_changelog_contents)
        self.scm.svn_server_realm = None
        self.assertEqual(self.scm.display_name(), "svn")
        self.assertEqual(self.scm.supports_local_commits(), False)
        self._setup_webkittools_scripts_symlink(self.scm)
        Checkout(self.scm).apply_patch(patch)
        self.assertRegexpMatches(self.scm.last_svn_commit_log(), 'fourth commit')
        self.assertRegexpMatches(self.scm.svn_commit_log(3), 'second commit')
        # FIXME: https://bugs.webkit.org/show_bug.cgi?id=111669
        # This test ends up looking in the actal $HOME/.subversion for authorization,
        # which makes it fragile. For now, set it to use a realm that won't be authorized,
        # but we should really plumb through a fake_home_dir here like we do in
        # test_has_authorization_for_realm.
        self.scm.svn_server_realm = '<http://svn.example.com:80> Example'
        result = self.scm.has_authorization_for_realm(realm, home_directory=fake_home_dir)
        self.assertFalse(self.scm.has_authorization_for_realm(SVN.svn_server_realm, home_directory=fake_home_dir))
        self.assertIn("test_file", self.scm.deleted_files())
        self.assertIn("test_file", self.scm.deleted_files())
        self.assertIn("test_file2", self.scm.deleted_files())
    def test_move(self):
        self._shared_test_move()

    def test_move_recursive(self):
        self._shared_test_move_recursive()

        self.assertIn("-some content", diff)
        self.assertIn("+changed content", diff)
        self.scm.discard_working_directory_changes()
        self.assertNotRegexpMatches(patch, r'Subversion Revision:')
        # If we cloned a git repo tracking an SVN repo, this would give the same result as
        scm.move('foo_file', 'bar_file')
        self.assertNotRegexpMatches(patch, r'rename from ')
        self.assertNotRegexpMatches(patch, r'rename to ')
        self.scm.svn_server_realm = None
        self.assertEqual(self.scm.display_name(), "git")
        self.assertEqual(self.scm.supports_local_commits(), True)
        self.assertNotRegexpMatches(run_command(['git', 'branch']), r'foo')
        self.assertNotRegexpMatches(diff_to_common_base, r'foo')
        self.assertRegexpMatches(diff_to_merge_base, r'foo')
        self.assertTrue(self.scm.rebase_in_progress())
        self.scm.discard_working_directory_changes()
        self.assertFalse(self.scm.rebase_in_progress())
        self.scm.discard_working_directory_changes()
        self.assertEqual(len(self.scm.commit_ids_from_commitish_arguments(['HEAD~2'])), 1)
        self.assertEqual(len(self.scm.commit_ids_from_commitish_arguments(['HEAD', 'HEAD~2'])), 2)
        self.assertRaises(ScriptError, self.scm.commit_ids_from_commitish_arguments, ['trunk...HEAD'])
        actual_commits = self.scm.commit_ids_from_commitish_arguments([commit_range])
        self._setup_webkittools_scripts_symlink(self.scm)
        Checkout(self.scm).apply_patch(patch)
        commit_text = self.scm.commit_with_message("yet another test commit")
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
    def test_locally_commit_all_working_copy_changes(self):
        self._local_commit('test_file', 'test content', 'test commit')
        write_into_file_at_path('test_file', 'changed test content')
        self.assertTrue(self.scm.has_working_directory_changes())
        self.scm.commit_locally_with_message('all working copy changes')
        self.assertFalse(self.scm.has_working_directory_changes())

    def test_locally_commit_no_working_copy_changes(self):
        self._local_commit('test_file', 'test content', 'test commit')
        write_into_file_at_path('test_file', 'changed test content')
        self.assertTrue(self.scm.has_working_directory_changes())
        self.assertRaises(ScriptError, self.scm.commit_locally_with_message, 'no working copy changes', False)

    def test_locally_commit_selected_working_copy_changes(self):
        self._local_commit('test_file_1', 'test content 1', 'test commit 1')
        self._local_commit('test_file_2', 'test content 2', 'test commit 2')
        write_into_file_at_path('test_file_1', 'changed test content 1')
        write_into_file_at_path('test_file_2', 'changed test content 2')
        self.assertTrue(self.scm.has_working_directory_changes())
        run_command(['git', 'add', 'test_file_1'])
        self.scm.commit_locally_with_message('selected working copy changes', commit_all_working_directory_changes=False)
        self.assertTrue(self.scm.has_working_directory_changes())
        self.assertTrue(self.scm.diff_for_file('test_file_1') == '')
        self.assertFalse(self.scm.diff_for_file('test_file_2') == '')

        self.assertItemsEqual(self.scm.revisions_changing_file('test_file_commit1'), [])
        self.assertRaises(AmbiguousCommitError, self.scm.commit_with_message, "yet another test commit")
        commit_text = self.scm.commit_with_message("yet another test commit", force_squash=True)
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertRegexpMatches(svn_log, r'test_file_commit2')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        commit_text = self.scm.commit_with_message("another test commit", git_commit="HEAD^")
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertNotRegexpMatches(svn_log, r'test_file_commit2')
        commit_text = self.scm.commit_with_message("another test commit", git_commit="HEAD~2..HEAD")
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertNotRegexpMatches(svn_log, r'test_file_commit0')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertRegexpMatches(svn_log, r'test_file_commit2')
        commit_text = self.scm.commit_with_message("another test commit")
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertRaises(AmbiguousCommitError, self.scm.commit_with_message, "another test commit")
        commit_text = self.scm.commit_with_message("another test commit", force_squash=True)
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertRegexpMatches(svn_log, r'test_file_commit2')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertRaises(ScriptError, self.scm.commit_with_message, "another test commit", git_commit="HEAD^")
        run_command(['git', 'config', 'webkit-patch.commit-should-always-squash', 'true'])
        commit_text = self.scm.commit_with_message("yet another test commit")
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertRegexpMatches(svn_log, r'test_file_commit2')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertRaises(AmbiguousCommitError, self.scm.commit_with_message, "yet another test commit")
        commit_text = self.scm.commit_with_message("yet another test commit", force_squash=True)
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertRegexpMatches(svn_log, r'test_file_commit2')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertRaises(AmbiguousCommitError, self.scm.commit_with_message, "another test commit")
        commit_text = self.scm.commit_with_message("another test commit", force_squash=True)
        self.assertEqual(self.scm.svn_revision_from_commit_text(commit_text), '6')
        self.assertNotRegexpMatches(svn_log, r'test_file2')
        self.assertRegexpMatches(svn_log, r'test_file_commit2')
        self.assertRegexpMatches(svn_log, r'test_file_commit1')
        self.assertRaises(ScriptError, self.scm.commit_with_message, "another test commit", force_squash=True)
        self.assertEqual(self.scm._upstream_branch(), 'my-branch')
        patch = self.scm.create_patch()
        self.assertRegexpMatches(patch, r'test_file_commit1')
        self.assertRegexpMatches(patch, r'test_file_commit2')
        patch = self.scm.create_patch()
        self.assertRegexpMatches(patch, r'test_file_commit2')
        self.assertRegexpMatches(patch, r'test_file_commit1')
        self.assertRegexpMatches(patch, r'Subversion Revision: 5')
        patch = self.scm.create_patch()
        self.assertRegexpMatches(patch, r'test_file_commit1')
        self.assertRegexpMatches(patch, r'Subversion Revision: 5')
        patch = self.scm.create_patch(changed_files=['test_file_commit2'])
        self.assertRegexpMatches(patch, r'test_file_commit2')
        patch = self.scm.create_patch()
        patch_with_changed_files = self.scm.create_patch(changed_files=['test_file_commit1', 'test_file_commit2'])
        self.assertEqual(patch, patch_with_changed_files)
        patch = self.scm.create_patch(git_commit="HEAD^")
        self.assertRegexpMatches(patch, r'test_file_commit1')
        self.assertNotRegexpMatches(patch, r'test_file_commit2')
        patch = self.scm.create_patch(git_commit="HEAD~2..HEAD")
        self.assertNotRegexpMatches(patch, r'test_file_commit0')
        self.assertRegexpMatches(patch, r'test_file_commit2')
        self.assertRegexpMatches(patch, r'test_file_commit1')
        patch = self.scm.create_patch(git_commit="HEAD....")
        self.assertNotRegexpMatches(patch, r'test_file_commit1')
        self.assertRegexpMatches(patch, r'test_file_commit2')
        patch = self.scm.create_patch()
        self.assertRegexpMatches(patch, r'test_file_commit2')
        self.assertRegexpMatches(patch, r'test_file_commit1')
        patch = self.scm.create_patch()
        self.assertNotRegexpMatches(patch, r'test_file2')
        self.assertRegexpMatches(patch, r'test_file_commit2')
        self.assertRegexpMatches(patch, r'test_file_commit1')
        patch = self.scm.create_patch()
        self.assertRegexpMatches(patch, r'\nliteral 0\n')
        self.assertRegexpMatches(patch, r'\nliteral 256\n')
        self._setup_webkittools_scripts_symlink(self.scm)

        patch_from_local_commit = self.scm.create_patch('HEAD')
        self.assertRegexpMatches(patch_from_local_commit, r'\nliteral 0\n')
        self.assertRegexpMatches(patch_from_local_commit, r'\nliteral 256\n')
        files = self.scm.changed_files()
        self.assertIn('test_file_commit1', files)
        self.assertIn('test_file_commit2', files)
        files = self.scm.changed_files('trunk..')
        self.assertIn('test_file_commit1', files)
        self.assertNotIn('test_file_commit2', files)
        files = self.scm.changed_files('trunk....')
        self.assertIn('test_file_commit1', files)
        self.assertIn('test_file_commit2', files)
        files = self.scm.changed_files(git_commit="HEAD^")
        self.assertIn('test_file_commit1', files)
        self.assertNotIn('test_file_commit2', files)
        files = self.scm.changed_files(git_commit="HEAD~2..HEAD")
        self.assertNotIn('test_file_commit0', files)
        self.assertIn('test_file_commit1', files)
        self.assertIn('test_file_commit2', files)
        files = self.scm.changed_files(git_commit="HEAD....")
        self.assertNotIn('test_file_commit1', files)
        self.assertIn('test_file_commit2', files)
        files = self.scm.changed_files()
        self.assertIn('test_file_commit2', files)
        self.assertIn('test_file_commit1', files)
        files = self.scm.changed_files()
        self.assertNotIn('test_file2', files)
        self.assertIn('test_file_commit2', files)
        self.assertIn('test_file_commit1', files)
        files = self.scm.changed_files()
        self.assertNotIn('test_file2', files)
        self.assertIn('test_file_commit2', files)
        self.assertIn('test_file_commit1', files)
        self.assertNotIn('test_file_commit1', files)
        self.assertIn('test_file_commit2', files)
        self.assertNotIn('test_file_commit0', files)
        self.assertNotIn('test_file_commit1', files)
        self.assertIn('test_file_commit2', files)
        self.assertIn('test_file_commit0', files)
        self.assertIn("test_file_commit1", self.scm.deleted_files())
        self.assertIn("test_file_commit1", self.scm.deleted_files())
        self.assertIn("test_file_commit2", self.scm.deleted_files())
    def test_move(self):
        self._shared_test_move()

    def test_move_recursive(self):
        self._shared_test_move_recursive()

        fullpath = os.path.realpath(os.path.join(self.git_checkout_path, relpath))
        self.assertIn("+Updated", diff)
        self.assertIn("-more test content", diff)
        self.assertIn("+Updated", cached_diff)
        self.assertIn("-more test content", cached_diff)
        self._shared_test_exists(self.scm, self.scm.commit_locally_with_message)
    maxDiff = None

        scm = Git(cwd=".", executive=MockExecutive(), filesystem=MockFileSystem())
        scm.read_git_config = lambda *args, **kw: "MOCKKEY:MOCKVALUE"
        expected_stderr = """\
MOCK run_command: ['git', 'merge-base', 'MOCKVALUE', 'HEAD'], cwd=%(checkout)s
MOCK run_command: ['git', 'diff', '--binary', '--no-color', '--no-ext-diff', '--full-index', '--no-renames', '', 'MOCK output of child process', '--'], cwd=%(checkout)s
MOCK run_command: ['git', 'rev-parse', '--show-toplevel'], cwd=%(checkout)s
MOCK run_command: ['git', 'log', '-1', '--grep=git-svn-id:', '--date=iso', './MOCK output of child process/MOCK output of child process'], cwd=%(checkout)s
""" % {'checkout': scm.checkout_root}
        OutputCapture().assert_outputs(self, scm.create_patch, expected_logs=expected_stderr)
        self.assertEqual(self.make_scm().push_local_commits_to_server(username='dbates@webkit.org', password='blah'), "MOCK output of child process")
    def test_timestamp_of_revision(self):
        scm = self.make_scm()
        scm.find_checkout_root = lambda path: ''
        scm._run_git = lambda args: 'Date: 2013-02-08 08:05:49 +0000'
        self.assertEqual(scm.timestamp_of_revision('some-path', '12345'), '2013-02-08T08:05:49Z')

        scm._run_git = lambda args: 'Date: 2013-02-08 01:02:03 +0130'
        self.assertEqual(scm.timestamp_of_revision('some-path', '12345'), '2013-02-07T23:32:03Z')

        scm._run_git = lambda args: 'Date: 2013-02-08 01:55:21 -0800'
        self.assertEqual(scm.timestamp_of_revision('some-path', '12345'), '2013-02-08T09:55:21Z')