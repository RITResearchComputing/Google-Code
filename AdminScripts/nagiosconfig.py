#!/usr/bin/python

# All of the defaults and exceptions to host configuration goes here

# Data structure constants
DEFAULTS = 'defaults'
EXCEPTIONS = 'exceptions'
SERVICE_NAME = 'service-name'
CHECK_COMMAND = 'check-command'
LIMIT_TO = 'limit-to'


x64b_nix_hosts = []
x32b_nix_hosts = [
    'epenguin-01.rit.edu', #NTID Video Wall
    'epenguin-02.rit.edu', #RC Lab (HD Sender)
    'epenguin-03.rit.edu', #Global Village Office
    'epenguin-04.rit.edu', #GCCIS CS Office (HD Sender)
    'epenguin-05.rit.edu', #College of Science SD
    'epenguin-06.rit.edu', #Saunders College of Business Atrium
    'epenguin-07.rit.edu', #RC Lab (Andrew)
    #'epenguin-08.rit.edu', #RC Lab (Network Testing)
    'epenguin-09.rit.edu', #Wallace Library (Sue Mee)
    'epenguin-10.rit.edu', #RC Lab Debian test(Temp)
    'epenguin-11.rit.edu', #VPR Office Global Village HD sender
    'epenguin-12.rit.edu', #NTID Video Wall HD Sender
    #'epenguin-13.rit.edu', #Lab pending rollout
    #'epenguin-14.rit.edu', #CSI Meeting Node
    #'epenguin-15.rit.edu', #RC Lab dead
    'epenguin-16.rit.edu', #CSI HD Sender
    #'epenguin-17.rit.edu', #RC Lab (formerly Izzie's)
    'epenguin-18.rit.edu', #SMFL HD Sender
    #'epenguin-19.rit.edu', #RC Lab (John)

    'lovelace.rit.edu', #Virtual host

    'ostrich-00.rit.edu', #Andrew's Testbed
    'ostrich-01.rit.edu', #Wallace Center
    #'ostrich-02.rit.edu', #BioMed Photo Lab (display)
    'ostrich-03.rit.edu', #RPL Send AND Recieve
    #'ostrich-04.rit.edu', #RC Lab intended for BioMed Photo Lab (sender)
    'ostrich-05.rit.edu', #CSI Video Wall 1
    'ostrich-06.rit.edu', #Innovation center kiosk
    'ostrich-07.rit.edu', #RACK
    'ostrich-08.rit.edu', #NTID Carey Lab
    'ostrich-09.rit.edu', #NTID GCCIS lab
    #'ostrich-10.rit.edu', #CSI Rack
    'ostrich-11.rit.edu', #CSI Rack Video Wall
    'ostrich-12.rit.edu', #CoB Dean's Office
    #'ostrich-13.rit.edu', #RC Lab intended for CBET Cadaver Lab
]

# This is used in the LIMIT_TO param of the check_sensors command definition
has_bad_or_no_sensors = [
    'lovelace.rit.edu',
    'ostrich-00.rit.edu',
    'ostrich-01.rit.edu',
    'ostrich-02.rit.edu',
    'ostrich-03.rit.edu',
    'ostrich-04.rit.edu',
    'ostrich-05.rit.edu',
    'ostrich-06.rit.edu',
    'ostrich-07.rit.edu',
    'ostrich-08.rit.edu',
    'ostrich-09.rit.edu',
    'ostrich-11.rit.edu',
    'ostrich-12.rit.edu',
]

# List of hosts that *should* be running drav
grav_hosts = [
    'epenguin-01.rit.edu',
    'epenguin-03.rit.edu',
    'epenguin-05.rit.edu',
    'epenguin-06.rit.edu',
    #'epenguin-09.rit.edu',
    #'epenguin-10.rit.edu',
    #'epenguin-11.rit.edu',
    #'epenguin-12.rit.edu',
    'ostrich-01.rit.edu',
    'ostrich-02.rit.edu',
    'ostrich-03.rit.edu',
    'ostrich-05.rit.edu',
    'ostrich-06.rit.edu',
    'ostrich-08.rit.edu',
    'ostrich-09.rit.edu',
    'ostrich-12.rit.edu',
    'epenguin-10.rit.edu', 
    'ostrich-11.rit.edu',
]

# List of hosts that *should* be running vic
vic_hosts = [
    'epenguin-02.rit.edu',
    'epenguin-04.rit.edu',
    'epenguin-12.rit.edu',
    'epenguin-11.rit.edu',
    'epenguin-16.rit.edu',
    'epenguin-18.rit.edu',
    'ostrich-02.rit.edu', #temporary
    'ostrich-03.rit.edu',
    'ostrich-04.rit.edu',
    'ostrich-06.rit.edu',
    'ostrich-08.rit.edu',
    'ostrich-09.rit.edu', 
    'epenguin-10.rit.edu',
]

# List of hosts that *should* be running gstreamer
gst_hosts = [ 
    'epenguin-05.rit.edu',
    'epenguin-06.rit.edu',
    'ostrich-07.rit.edu', 
    'epenguin-10.rit.edu',
]

# None right now
all_win_hosts = []

host_base, service_base = {}, {}
for h in x64b_nix_hosts:
    host_base[h] = 'rc-server'
    service_base[h] = 'rc-service'

for h in x32b_nix_hosts:
    host_base[h] = 'ag-server'
    service_base[h] = 'ag-service'

for h in all_win_hosts:
    host_base[h] = 'ag-server'
    service_base[h] = 'ag-service'

all_nix_hosts = x64b_nix_hosts + x32b_nix_hosts
all_hosts = all_nix_hosts + all_win_hosts

ag_sending_nodes = [
    'epenguin-06.rit.edu',
    #'epenguin-08.rit.edu',
    #'penguin-04.rit.edu',
]

critical_hosts = ['lovelace.rit.edu']

# All ICELAB machines are physical
physical_hosts = all_nix_hosts

# ICELAB doesn't have any virtual machines, so these are empty
virt_heads = []
virt_guests_mapping = {}

nagios_hosts = []
# You have no sge or slurm installations.  Don't worry about it.
# Its here for posterity.
sge_heads = []
sge_nodes = []
slurm_heads = []
slurm_nodes = []

web_servers = {
    'lovelace.rit.edu' : [
        [False, 'lovelace.rit.edu'],
    ],
}
sql_servers = {}

hostgroups = {
    'ag-sending-nodes' : {
        'alias' : 'AG Sending Nodes',
        'members' : ag_sending_nodes,
    },
    #'physical' : {
    #    'alias' : 'Physical Machines',
    #    'members' : physical_hosts,
    #},
    'virtual' : {
        'alias' : 'Virtual Machines',
        'members' : [h for h in all_nix_hosts if not h in physical_hosts],
    },
    'critical' : {
        'alias' : 'Critical Machines',
        'members' : critical_hosts,
    },
    'noncritical' : {
        'alias' : 'Non-critical Machines',
        'members' : [h for h in all_hosts if not h in critical_hosts],
    },
    'nix' : {
        'alias' : '*nix Machines',
        'members' : all_nix_hosts,
    },
    'libvirt' : {
        'alias' : 'Virtualizers',
        'members' : virt_heads,
    },
    #'win' : {
    #    'alias' : 'win machines',
    #    'members' : all_win_hosts,
    #},
    'web' : {
        'alias' : 'Web Servers',
        'members' : web_servers.keys(), # Its a dict!
    },
    'nagios' : {
        'alias' : 'Nagios Servers', 
        'members' : nagios_hosts,
    },
    #'sql' : {
    #    'alias' : 'SQL Servers',
    #    'members' : sql_servers.keys(), # Its a dict!
    #},
    #'64bit' : {
    #    'alias' : '64 bit machines',
    #    'members' : x64b_nix_hosts,
    #},
    '32bit' : {
        'alias' : '32 bit machines',
        'members' : x32b_nix_hosts,
    },
    'ICE/CASCI' : {
        'alias' : 'ICE/CASCI machines',
        'members' : x32b_nix_hosts + all_win_hosts,
    },
}


win_service_parameters = {
    'ping' : {
        DEFAULTS : [100.0, "20%", 500.0, "60%"],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Ping',
        CHECK_COMMAND : 'check_ping!%f,%s!%f,%s',
    },
    'check_vic' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'VIC',
        CHECK_COMMAND : 'check_nrpe_no_args!check_vic',
        LIMIT_TO : all_win_hosts,
    },
    'check_rat' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'RAT',
        CHECK_COMMAND : 'check_nrpe_no_args!check_rat',
        LIMIT_TO : [],
    },
    'check_dvts' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'DVTS',
        CHECK_COMMAND : 'check_nrpe_no_args!check_dvts',
        LIMIT_TO : [],
    },
}

nix_service_parameters = {
    'check_sensors' : {
        DEFAULTS : [],
        EXCEPTIONS : {},
        SERVICE_NAME : 'CPU Sensors',
        CHECK_COMMAND : 'check_nrpe_no_args!check_sensors',
        LIMIT_TO : [
            h for h in x32b_nix_hosts if h not in has_bad_or_no_sensors
        ],
    },
    'check_vic' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'VIC',
        CHECK_COMMAND : 'check_nrpe_no_args!check_vic',
        LIMIT_TO : vic_hosts,
    },
    'check_rat' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'RAT',
        CHECK_COMMAND : 'check_nrpe_no_args!check_rat',
        LIMIT_TO : [
            'ostrich-03.rit.edu',
            'ostrich-06.rit.edu',
            'epenguin-10.rit.edu',
        ],
    },
    'check_dvts' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'DVTS',
        CHECK_COMMAND : 'check_nrpe_no_args!check_dvts',
        LIMIT_TO : [], # NOTE -- no hosts use dvts at the moment
    },
    'check_grav' : {
        DEFAULTS : [1],
	    EXCEPTIONS : {
		'ostrich-11.rit.edu' : [3],
	    },
        SERVICE_NAME : 'GRAV',
        CHECK_COMMAND : 'check_nrpe!check_grav!%i',
        LIMIT_TO : grav_hosts,
    },
    'check_gst' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'GStreamer',
        CHECK_COMMAND : 'check_nrpe_no_args!check_gst',
        LIMIT_TO : gst_hosts,
    },
    'root-fs-ro' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'Root_FS_is_read-only',
        CHECK_COMMAND : 'check_nrpe_no_args!check_root',
        LIMIT_TO : [h for h in all_nix_hosts if not h in physical_hosts],
    },
    'nagios' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'Nagios_Itself',
        CHECK_COMMAND : 'check_nrpe_no_args!check_nagios',
        LIMIT_TO : nagios_hosts,
    },
    'ping' : {
        DEFAULTS : [100.0, "20%", 500.0, "60%"],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Ping',
        CHECK_COMMAND : 'check_ping!%f,%s!%f,%s',
    },
    'disk' : {
        DEFAULTS : ["20%", "10%", "/dev/disk"],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Root_Partition',
        CHECK_COMMAND : 'check_nrpe!check_disk!%s!%s!%s',
    },
    'user' : {
        DEFAULTS : [10, 15],
        EXCEPTIONS : {
            'brodie' : [20, 30],
            'epenguin-07.rit.edu' : [15, 20],
        },
        SERVICE_NAME : 'Current_Users',
        CHECK_COMMAND : 'check_nrpe!check_users!%i!%i',
    },
    'check-for-proc' : {
        DEFAULTS : None,
        EXCEPTIONS : {
            'media' : ['QuickBridge'],
        },
        SERVICE_NAME : 'Check for process',
        CHECK_COMMAND : 'check_nrpe!check_for_proc!%s',
        LIMIT_TO : ['media'],
    },
    'procs-per-user' : { #[Critical, Warning]
        DEFAULTS : [100, 160],
        EXCEPTIONS : {
        },
        SERVICE_NAME : 'Procs_per_User',
        CHECK_COMMAND : 'check_nrpe!check_procs_custom!%i!%i',
    },
    'user-unique' : {
        DEFAULTS : [5, 10],
        EXCEPTIONS : {
            'brodie'    : [10, 15],
            'solvay'    : [8,  12],
            'werner'    : [8,  12],
        },
        SERVICE_NAME : 'Current_Unique_Users',
        CHECK_COMMAND : 'check_nrpe!check_users_custom!%i!%i',

    },
    'zombie' : {
        DEFAULTS : [5, 10],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Zombie_Processes',
        CHECK_COMMAND : 'check_nrpe!check_zombie_procs!%i!%i',
    },
    'total-procs' : { #[Critical, Warning]
        DEFAULTS : [280, 300],
        EXCEPTIONS : {
            'ostrich-00.rit.edu'    : [300, 350],
            'ostrich-07.rit.edu'    : [300, 350],
        },
        SERVICE_NAME : 'Total_Processes',
        CHECK_COMMAND : 'check_nrpe!check_total_procs!%i!%i',
    },
    'load' : {
        DEFAULTS : ['6,5,4', '7,6,5'],
        EXCEPTIONS : {
        },
        SERVICE_NAME : 'Current_Load',
        CHECK_COMMAND : 'check_nrpe!check_load!%s!%s'
    },
    'swap' : {
        DEFAULTS : ['20%', '10%'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Swap_Usage',
        CHECK_COMMAND : 'check_nrpe!check_swap!%s!%s',
    },
    'time' : {
        DEFAULTS : [30, 60],
        EXCEPTIONS : {
        },
        SERVICE_NAME : 'NTP_Sync',
        CHECK_COMMAND : 'check_nrpe!check_ntp_time!ntp.rit.edu!%i!%i',
    },
}

for host, guests in virt_guests_mapping.iteritems():
    for guest in guests:
        addition = {
            'check_virt_%s_for_%s' % (host, guest) : {
                DEFAULTS: [guest],   EXCEPTIONS: {},
                SERVICE_NAME: 'Check_virt_%s_for_%s' % (host, guest),
                CHECK_COMMAND: 'check_nrpe!check_virt_guest!%s',
                LIMIT_TO: [host],
            }
        }
        nix_service_parameters.update(addition)
