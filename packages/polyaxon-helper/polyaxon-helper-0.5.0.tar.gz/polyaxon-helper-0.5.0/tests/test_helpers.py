# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import json
import os
import uuid
from unittest import TestCase

from polyaxon_client import settings

from polyaxon_helper import (
    get_cluster_def,
    get_data_paths,
    get_declarations,
    get_experiment_info,
    get_job_info,
    get_log_level,
    get_outputs_path,
    get_outputs_refs_paths,
    get_task_info,
    get_tf_config
)


class TestHelpers(TestCase):
    def setUp(self):
        settings.IN_CLUSTER = True

    @staticmethod
    def check_empty_value(key, expected_function):
        os.environ.pop(key, None)
        assert expected_function() is None

    @staticmethod
    def check_non_dict_value(key, expected_function, value='non dict random value'):
        os.environ[key] = value
        assert expected_function() is None

    @staticmethod
    def check_valid_dict_value(key, expected_function, value):
        os.environ[key] = json.dumps(value)
        assert expected_function() == value

    @staticmethod
    def check_valid_value(key, expected_function, value):
        os.environ[key] = value
        assert expected_function() == value

    def test_empty_cluster_def(self):
        self.check_empty_value('POLYAXON_CLUSTER', get_cluster_def)

    def test_non_dict_cluster_def(self):
        self.check_non_dict_value('POLYAXON_CLUSTER', get_cluster_def)

    def test_dict_cluster_def(self):
        cluster_def = {
            "master": ["plxjob-master0-8eefb7a1146f476ca66e3bee9b88c1de:2000"],
            "worker": ["plxjob-worker1-8eefb7a1146f476ca66e3bee9b88c1de:2000",
                       "plxjob-worker2-8eefb7a1146f476ca66e3bee9b88c1de:2000"],
            "ps": ["plxjob-ps3-8eefb7a1146f476ca66e3bee9b88c1de:2000"],
        }
        self.check_valid_dict_value('POLYAXON_CLUSTER', get_cluster_def, cluster_def)

    def test_empty_declarations(self):
        self.check_empty_value('POLYAXON_PARAMS', get_declarations)

    def test_non_dict_declarations(self):
        self.check_non_dict_value('POLYAXON_PARAMS', get_declarations)

    def test_dict_declarations(self):
        declarations = {
            "foo": "bar"
        }
        self.check_valid_dict_value('POLYAXON_PARAMS', get_declarations, declarations)

    def test_empty_experiment_info(self):
        self.check_empty_value('POLYAXON_EXPERIMENT_INFO', get_experiment_info)

    def test_non_dict_experiment_info(self):
        self.check_non_dict_value('POLYAXON_EXPERIMENT_INFO', get_experiment_info)

    def test_dict_experiment_info(self):
        experiment_info = {
            "project_name": "project_bar",
            "experiment_group_name": None,
            "experiment_name": "project_bar.1",
            "project_uuid": uuid.uuid4().hex,
            "experiment_group_uuid": None,
            "experiment_uuid": uuid.uuid4().hex,
        }
        self.check_valid_dict_value('POLYAXON_EXPERIMENT_INFO',
                                    get_experiment_info,
                                    experiment_info)

    def test_empty_job_info(self):
        self.check_empty_value('POLYAXON_JOB_INFO', get_job_info)

    def test_non_dict_job_info(self):
        self.check_non_dict_value('POLYAXON_JOB_INFO', get_job_info)

    def test_dict_job_info(self):
        job_info = {
            "project_name": "project_bar",
            "job_name": "project_bar.jobs.1",
            "project_uuid": uuid.uuid4().hex,
            "job_uuid": uuid.uuid4().hex,
        }
        self.check_valid_dict_value('POLYAXON_JOB_INFO',
                                    get_job_info,
                                    job_info)

    def test_empty_task_info(self):
        self.check_empty_value('POLYAXON_TASK_INFO', get_task_info)

    def test_non_dict_task_info(self):
        self.check_non_dict_value('POLYAXON_TASK_INFO', get_task_info)

    def test_dict_task_info(self):
        task_info = {"type": 'master', "index": 0}
        self.check_valid_dict_value('POLYAXON_TASK_INFO',
                                    get_task_info,
                                    task_info)

    def test_empty_outputs_path(self):
        self.check_empty_value('POLYAXON_RUN_OUTPUTS_PATH', get_outputs_path)

    def test_valid_outputs_path(self):
        self.check_valid_value('POLYAXON_RUN_OUTPUTS_PATH', get_outputs_path, 'path')

    def test_empty_data_path(self):
        self.check_empty_value('POLYAXON_RUN_DATA_PATHS', get_data_paths)

    def test_valid_data_path(self):
        self.check_valid_dict_value('POLYAXON_RUN_DATA_PATHS', get_data_paths, {'data': 'path'})

    def test_empty_outputs_refs_paths(self):
        self.check_empty_value('POLYAXON_REFS_OUTPUTS_PATHS', get_outputs_refs_paths)

    def test_valid_data_path_with_ref(self):
        self.check_valid_dict_value('POLYAXON_REFS_OUTPUTS_PATHS',
                                    get_outputs_refs_paths,
                                    {
                                        'jobs': ['path1', 'path12'],
                                        'experiments': ['path1', 'path12']
                                     })

    def test_empty_tf_config(self):
        assert get_tf_config() == {
            'cluster': None,
            'task': None,
            'model_dir': None,
            'environment': 'cloud'
        }

    def test_non_dict_tf_config(self):
        os.environ['POLYAXON_CLUSTER'] = 'value'
        os.environ['POLYAXON_TASK_INFO'] = 'value'
        assert get_tf_config() == {
            'cluster': None,
            'task': None,
            'model_dir': None,
            'environment': 'cloud'
        }

    def test_dict_tf_config(self):
        cluster_def = {
            "master": ["plxjob-master0-8eefb7a1146f476ca66e3bee9b88c1de:2000"],
            "worker": ["plxjob-worker1-8eefb7a1146f476ca66e3bee9b88c1de:2000",
                       "plxjob-worker2-8eefb7a1146f476ca66e3bee9b88c1de:2000"],
            "ps": ["plxjob-ps3-8eefb7a1146f476ca66e3bee9b88c1de:2000"],
        }
        task_info = {"type": 'master', "index": 0}
        os.environ['POLYAXON_CLUSTER'] = json.dumps(cluster_def)
        os.environ['POLYAXON_TASK_INFO'] = json.dumps(task_info)
        os.environ['POLYAXON_RUN_OUTPUTS_PATH'] = 'path'
        assert get_tf_config() == {
            'cluster': cluster_def,
            'task': {"type": 'master', "index": 0},
            'model_dir': 'path',
            'environment': 'cloud'
        }

    def test_empty_log_level(self):
        self.check_empty_value('POLYAXON_LOG_LEVEL', get_log_level)

    def test_valid_log_level(self):
        self.check_valid_value('POLYAXON_LOG_LEVEL', get_log_level, 'info')
