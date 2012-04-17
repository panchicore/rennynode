from django.core.management.base import BaseCommand, CommandError
from rennynode import settings
from rennynode.linode import api, oop
from rennynode.linode.oop import *
from time import clock

class Command(BaseCommand):

    def handle(self, *args, **options):

        linode = api.Api(settings.LINODE_API_KEY)
        oop.ActiveContext = linode
        print 'Connecting...'

        i = 1
        for server in Linode.list():
            print "%i. rebooting server %s" % (i, server.label)
            server.reboot()
            print ">>> Payload deployed."
            i += 1

        print "Calling to renny to cellphone... timeout error: Renny N.V.V."



