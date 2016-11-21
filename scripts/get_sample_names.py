#!/usr/bin/env python

import couchdb
import argparse
import os
import yaml

import LIMS2DB.utils as lutils

def main(args):

    with open(os.path.expanduser('~/opt/config/post_process.yaml')) as conf_file:
        conf=yaml.load(conf_file)
    couch=lutils.setupServer(conf)
    db=couch['projects']
    view=db.view('samples/customer_names')
    for row in view[args.project]:
        d=row.value

    for sample in sorted(d.keys()):
        print "{}\t{}".format(sample, d[sample])


if __name__ == "__main__":

    desc = ("Prints internal sample names and customer names side by side")
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-p', '--project', dest="project",
                        help=('print samples for the given project'))
    args=parser.parse_args()
    main(args)
