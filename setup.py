project="main.py"

from distutils.core import setup
import py2exe # Patching distutils setup



setup(
        windows=[{
                    'script':project,
                    'icon_resources': [(1, "joypad.ico")],
                  }
                ],
        options = {
                    "py2exe":{
                                "includes":["sip",'serial.urlhandler.protocol_hwgrep', 
								'serial.urlhandler.protocol_rfc2217',
								'serial.urlhandler.protocol_socket', 
								'serial.urlhandler.protocol_loop',
								'guidata',
								'guiqwt',
											],
                                
                                'excludes': ['_gtkagg', '_tkagg','PyQt4.uic.port_v3','javax.comm',
								'serialposix','serialjava','serialcli'],
                                "dll_excludes":["MSVCP90.dll",'libzmq.dll','libiomp5md.dll',
                                                'libifcoremd.dll','libmmd.dll' , 
                                                'svml_dispmd.dll','libifportMD.dll']
                             }
                  },
                 
     )