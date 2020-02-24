import os
import sys
from optparse import OptionParser
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)
from GovOpendata.apps import app, initialize

def main():
    opts, args = parse_opts(app.config)
    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI=opts.database_url,
    ))
    initialize()
    app.run(host=opts.host, port=opts.port, use_reloader=False, threaded=True, debug=True)


def parse_opts(config):
    parser = OptionParser(usage="%prog [options]",
                          description="Admin ui for spider service")
    parser.add_option("--host",
                      help="host, default:0.0.0.0",
                      dest='host',
                      default='0.0.0.0')
    parser.add_option("--port",
                      help="port, default:5000",
                      dest='port',
                      type="int",
                      default=5000)
    parser.add_option("--database-url",
                      help='SpiderKeeper metadata database default: %s' % config.get('SQLALCHEMY_DATABASE_URI'),
                      dest='database_url',
                      default=config.get('SQLALCHEMY_DATABASE_URI'))


    return parser.parse_args()


if __name__ == '__main__':
    main()