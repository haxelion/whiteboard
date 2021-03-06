from graph.models import Category
from keywords.models import Keyword
from agora.models import Thread
from course.models import Course

from django.core.management.base import BaseCommand

cat = Category.objects.create

class Command(BaseCommand):
    help = """Fills database with realistic data"""
    def handle(self, *args, **options):
        toplevel = cat(name="P402", description="P402::Whiteboard")

        science = cat(name="Fac Sciences", description="Faculte des sciences")
        toplevel.attach(science)

        ### Computing section
        computing = cat(name="Sc. Info", description="Sciences Informatiques")
        science.attach(computing)

        ba1info = cat(name="BA1 Sc. Info", description="Bachelier 1 en Sciences Informatiques")
        computing.attach(ba1info)
        computing.attach(cat(name="BA2 Sc. Info", description="Bachelier 1 en Sciences Informatiques"))
        computing.attach(cat(name="BA3 Sc. Info", description="Bachelier 3 en Sciences Informatiques"))
        computing.attach(cat(name="MA1 Sc. Info", description="Master 1 en Sciences Informatiques"))
        computing.attach(cat(name="MA2 Sc. Info", description="Master 2 en Sciences Informatiques"))
        ba1infopt = cat(name="Options", description="Cours aux choix")
        ba1info.attach(ba1infopt)

        ### Math section
        math = cat(name="Sc. Math", description="Sciences Mathematiques")
        science.attach(math)

        ba1math = cat(name="BA1 Sc. Math", description="Bachelier 1 en Sciences Mathematiques")
        math.attach(ba1math)
        math.attach(cat(name="BA2 Sc. Math", description="Bachelier 2 en Sciences Mathematiques"))
        math.attach(cat(name="BA3 Sc. Math", description="Bachelier 3 en Sciences Mathematiques"))
        math.attach(cat(name="MA1 Sc. Math", description="Master 1 en Sciences Mathematiques"))
        math.attach(cat(name="MA2 Sc. Math", description="Master 2 en Sciences Mathematiques"))
        ba1matopt = cat(name="Options", description="Cours aux choix")
        ba1math.attach(ba1matopt)

        ### Polytechnic school
        polytek = cat(name="Polytech", description="Ecole polytechnique de Bruxelles")
        toplevel.attach(polytek)

        ba1poly = cat(name="BA1 Polytech", description="Bachelier 1 en Polytechnique")
        polytek.attach(ba1poly)
        polytek.attach(cat(name="BA2 Polytech", description="Bachelier 2 en Polytechnique"))
        polytek.attach(cat(name="BA3 Polytech", description="Bachelier 3 en Polytechnique"))
        polytek.attach(cat(name="MA1 Polytech", description="Master 1 en Polytechnique"))
        polytek.attach(cat(name="MA2 Polytech", description="Master 2 en Polytechnique"))

        ### Courses
        infof101 = Course.objects.create(
            mnemonic='INFO-F-101', name='Programmation 1', teacher='tmassart@ulb.ac.be',
            description='Introduction a la programmation en Python'
        )
        ba1math.attach(infof101)
        ba1info.attach(infof101)
        ba1poly.attach(infof101)

        infof102 = Course.objects.create(
            mnemonic='INFO-F-102', name='Fonctionnement des ordinateurs',
            teacher='gilles.geeraerts@ulb.ac.be',
            description='Etude approfondie des systemes informatiques'
        )
        ba1math.attach(infof102)
        ba1info.attach(infof102)

        mathf110 = Course.objects.create(
            mnemonic='MATH-F-110', name='Problemes et methodes en mathematiques',
            teacher='fbourgeo@ulb.ac.be',
            description='Etude ludique de celebres problemes mathematiques'
        )
        ba1infopt.attach(mathf110)
        ba1matopt.attach(mathf110)

        mathf111 = Course.objects.create(
            mnemonic='MATH-F-110', name='Logiciels mathematiques',
            teacher='nrichard@ulb.ac.be',
            description='Etude de logiciel(s) de calcul symbolique'
        )
        ba1infopt.attach(mathf111)
        ba1math.attach(mathf111)

        ### Threads
        discussion = Thread.objects.create(name="[Projet] Priorite des pipelines")
        for kw in ['projet', 'pipeline', 'multivac']:
            discussion.add_keyword(kw)
        infof102.attach(discussion)
        discussion.reply(text="Dans mon algorithme, je fais avancer les pipelines un par un separement. Dois-je respecter un ordre particulier ?")
        discussion.reply(text="A toi de voir selon ton algorithme")

        discussion = Thread.objects.create(name="[Projet 2] Quand faire avancer les voitures sur l'autoroute ?")
        discussion.add_keyword('projet')
        infof101.attach(discussion)

