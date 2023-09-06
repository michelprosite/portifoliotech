from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
import uuid

# Create your models here.
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)    
    
    class Meta:
        abstract = True


class BoasVindas(Base):
    titulo = models.CharField('Titulo', max_length=100)
    mensagem = models.TextField('Mensagem', max_length=2000)
    link = models.URLField('Link')
    textButtom = models.CharField('Texto do Botão', max_length=50)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': (450, 225)})
    slug = models.SlugField('Slug', max_length=1000, blank=True, editable=False)
    
    class Meta:
        verbose_name = 'BoaVinda'
        verbose_name_plural = 'BoasVindas'

    def __str__(self):
        return self.titulo


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(produto_pre_save, sender=BoasVindas)


class Academico(Base):
    curso = models.CharField("Curso", max_length=100)
    instituicao = models.CharField("Instituição", max_length=100)
    dataInicio = models.DateField("Data início")
    dataConclusao = models.DateField("Data Conclusão")
    descricaoP1 = models.TextField("Descrição 1/3", max_length=2000)
    descricaoP2 = models.TextField("Descricao 2/3", max_length=2000, blank=True)
    descricaoP3 = models.TextField("Descrição 3/3", max_length=2000, blank=True)
    textButtom = models.CharField("Texto Botão", max_length=50)
    
    class Meta:
        verbose_name = 'Acadêmico'
        verbose_name_plural = 'Acadêmico'

    def __str__(self):
        return self.curso
    

class Projetos(Base):
    titulo = models.CharField('Título', max_length=100)
    comentario = models.TextField('Comentário')
    urlgit = models.URLField('URL GitHub')
    urlsite = models.URLField('URL Site')
    dataConclusao = models.DateField('Data Conclusão')
    cargaHoraria = models.IntegerField("Carga Horária")
    peso = models.IntegerField("Peso do Projeto")
    imagem = StdImageField("Imagem", upload_to=get_file_path,
                           variations={"thumb": (450, 225)})
    slug = models.SlugField('Slug', max_length=1000, blank=True, editable=False)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(produto_pre_save, sender=Projetos)


class Certificados(Base):
    titulo = models.CharField('Título', max_length=100)
    instituicao = models.CharField("Instituição", max_length=100)
    urlValidacao = models.URLField('URL Validação')
    dataConclusao = models.DateField('Data Conclusão')
    cargaHoraria = models.IntegerField("Carga Horária")
    imagem = StdImageField("Imagem", upload_to=get_file_path,
                           variations={"thumb": (450, 225)})
    slug = models.SlugField('Slug', max_length=1000, blank=True, editable=False)

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return self.titulo


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(produto_pre_save, sender=Certificados)



TECNOLOGIAS_CHOICES = (
('fa-brands fa-python', 'Python'),
('fa-brands fa-html5', 'HTML 5'),
('fa-brands fa-css3-alt', 'CSS 3'),
('fa-solid fa-database', 'SQL'),
('fa-solid fa-file-excel', 'Excel'),
('fa-brands fa-square-js', 'JavaScript'),
('fa-solid fa-spider', 'Web Scraper'),
('fa-brands fa-linux', 'Linux'),
('fa-brands fa-windows', 'Windows'),
('fa-brands fa-git-alt', 'Git'),
('fa-solid fa-chart-simple', 'Data Analitics'),
('fa-solid fa-repeat', 'CRISP-DM'),
('fa-solid fa-users-gear', 'Scrum'),
)

class Conhecimentos(Base):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    nivel = models.IntegerField("Nivel de Conhecimento 0-10")
    icone = models.CharField("Font Awesome", max_length=300, choices=TECNOLOGIAS_CHOICES)
