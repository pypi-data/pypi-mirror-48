#!/usr/bin/env python3
from optparse import OptionParser

import pickle
import logging
import datetime
import os
from os import listdir
from os.path import isfile, join, exists
from plumbum.cmd import git
import yaml


VERBOSE_FLAG = False
EXECUTABLE_FLAG = False
__version__ = '1.8'


def get_project_name(current_dir, script_path) -> str:
    project_name = ''
    if exists(join(current_dir, ".git")):
        full_projectname = git["config", "--get", "remote.origin.url"]()
    else:
        full_projectname = current_dir

    project_name = full_projectname.split("/")[-1].replace(".git", "")

    return project_name


def edit_template_string(template_str, file_prefix, project_name, config_path) -> str:

    replace_pairs = {}
    now = datetime.datetime.now()
    date = ("{}-{}-{}".format(now.month, now.day, now.year))
    configs = yaml.load(open(config_path, "r+"))
    replace_pairs["<date>"] = date
    replace_pairs["<filename>"] = file_prefix
    replace_pairs["<project>"] = project_name
    replace_pairs["<email>"] = configs["email"]
    replace_pairs["<name>"] = configs["name"]

    for pattern, replacement in replace_pairs.items():
        template_str = template_str.replace(pattern, replacement)

    return template_str


def config():
    template_filenames = [f for f in listdir(
        "templates") if isfile(join("templates", f))]

    templates_dict = {}
    for filename in template_filenames:
        template = open(join("templates", filename), "rb")
        file_extention = filename.split('.')[-1]
        templates_dict[file_extention] = template.read()

    filename = 'templates.pickle'
    outfile = open(filename, 'wb')

    pickle.dump(templates_dict, outfile)
    outfile.close()

    print("Starting user configuration...")
    name = input("Name:")
    email = input("Email address [or github URL] :")

    configs = {"name": name, "email": email}
    config_file = open("config.yaml", "w")
    yaml.dump(configs, config_file, default_flow_style=False)


def main(args):
    filename = args[0]
    script_path = os.path.dirname(os.path.realpath(__file__))
    pickle_filename = join(script_path, "templates.pickle")
    print(pickle_filename, isfile(pickle_filename))
    if filename == "setup" or not isfile(pickle_filename):
        config()
        return
    templates_pickle = open(pickle_filename, 'rb')
    file_extention = filename.split('.')[-1]
    curr_path = os.getcwd()

    templates_dict = pickle.load(templates_pickle)
    template_string = templates_dict[file_extention].decode('UTF-8')

    config_path = join(script_path, "config.yaml")
    project_name = get_project_name(curr_path, script_path)
    file_prefix = filename.split('.')[0]
    with open(filename, 'w+') as output:
        output.write(edit_template_string(template_string,
                                          file_prefix, project_name, config_path))
        output.close()


def nft():
    parser = OptionParser(usage="usage: $./nft [options] <filename>",
                          version="%prog 0.1")
    parser.add_option("-x", "--eXecutable",
                      action="store_true",
                      dest="x_flag",
                      default=False,
                      help="Chmods the file so it is an executable")
    parser.add_option("-v", "--verbose",
                      action="store_true",
                      dest="v_flag",
                      default=False,
                      help="Verbose mode",)
    (options, args) = parser.parse_args()
    options_dict = vars(options)
    EXECUTABLE_FLAG = options_dict['x_flag']
    VERBOSE_FLAG = options_dict['v_flag']
    if len(args) != 1:
        logging.error("Needed one file name but found " + str(len(args)))
    main(args)
