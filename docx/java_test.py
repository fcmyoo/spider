import os

from jpype import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jar_path = os.path.join(BASE_DIR, 'aspose.jar')
if not isJVMStarted():
    startJVM(getDefaultJVMPath(), '-ea',"-Djava.class.path=%s" % jar_path)
    system = JClass('com.aspose.words.Document')
    prop = " yourProperty "
    value ='yourValue '
    system.setProperty(str(prop),str(value))

