from diagrams import Diagram, Cluster

from diagrams.k8s.compute import Pod
from diagrams.k8s.network import SVC, Ing
from diagrams.k8s.storage import PV, PVC, Vol
from diagrams.k8s.group import Namespace


with Diagram("k8s Architecture", show=False):

    fe_ing = Ing("https//my-whiteapp.fr")

    with Cluster("White App"):

        nm = Namespace("WhiteApp")

        # Services
        fe_svc = SVC("")
        be_svc = SVC("")
        db_svc = SVC("")

        # Pods
        fe_pod = Pod("FrontEnd")
        be_pod = Pod("Backend")
        db_pod = Pod("Database")

        # Storage
        db_vol = Vol("DB Volume")
        be_vol = Vol("BE Volume")


    fe_ing >> fe_svc

    fe_svc >> fe_pod
    be_svc >> be_pod
    db_svc >> db_pod

    fe_pod >> be_svc
    be_pod >> db_svc
    
    db_pod >> db_vol
    be_pod >> be_vol

    