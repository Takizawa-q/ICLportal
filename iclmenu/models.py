from django.db import models

class AboutSection(models.Model):
    cennosti = models.TextField(default="ICL это: Открытость, доверие, инновации")
    structure = models.TextField(default="Крупнейшая ИТ-компания России")
    history = models.TextField(default="Основана в: 1991 году одним из крупнейших производителей вычислительных комплексов (ЭВМ) в СССР Казанским производственным объединением вычислительных систем (КПО ВС) и крупнейшим производителем компьютеров Великобритании International Computers Limited (ICL) было создано советско-британское совместное предприятие «ICL-КПО ВС», зарегистрированное 2 июля 1991 года в Министерстве финансов РСФСР.")
    
class LearningSection(models.Model):
    title = models.TextField(default="Раздел")
    link_1_href = models.TextField(default="#")
    link_1_view = models.TextField(default="Ссылка")
    
    link_2_href = models.TextField(default="#")
    link_2_view = models.TextField(default="Ссылка")
    
    link_3_href = models.TextField(default="#")
    link_3_view = models.TextField(default="Ссылка")
    
    
    
class LinksSection(models.Model):
    title = models.TextField(default="Раздел")
    link_1_href = models.TextField(default="#")
    link_1_view = models.TextField(default="Ссылка")
    
    link_2_href = models.TextField(default="#")
    link_2_view = models.TextField(default="Ссылка")
    
    link_3_href = models.TextField(default="#")
    link_3_view = models.TextField(default="Ссылка")
    
class InstructionsSection(models.Model):
    title = models.TextField(default="Раздел инструкций")
    
    link_1_href = models.TextField(default="#")
    link_1_view = models.TextField(default="Ссылка")
    
    link_2_href = models.TextField(default="#")
    link_2_view = models.TextField(default="Ссылка")
    
    link_3_href = models.TextField(default="#")
    link_3_view = models.TextField(default="Ссылка")
    
    
    

