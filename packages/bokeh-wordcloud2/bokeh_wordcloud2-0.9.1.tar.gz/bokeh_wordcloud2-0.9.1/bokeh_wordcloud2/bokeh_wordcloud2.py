import math
from bokeh.core.property.container import Array, List
from bokeh.core.property.either import Either
from bokeh.core.property.enum import Enum
from bokeh.core.property.instance import Instance
from bokeh.core.property.primitive import String, Float, Int
from bokeh.events import Event
from bokeh.models import DataSource, CDSView, Widget, CustomJS, Callback, ColumnDataSource,Button
# from bokeh.sphinxext.util import



class WordClick(Event):
    '''
    Custom Event that is fired when the user clicks a word
    '''
    event_name = 'word_click_event'
    word=None
    weight=None
    def __init__(self, model,word,weight):
        if model is not None and not isinstance(model, WordCloud2):
            msg ='{clsname} event only applies to button models'
            raise ValueError(msg.format(clsname=self.__class__.__name__))
        self.word=word
        self.weight=weight

        super(WordClick, self).__init__(model=model)
    def __str__(self):
        return "<WordClickEvent word=%r weight=%r>"%(self.word,self.weight)
    def __repr__(self):
        return str(self)

class _WordCloud2Meta(Widget):
    __implementation__ = "typescript/extension_bokeh_wordcloud2.ts"
    __javascript__ = [
        "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/wordcloud2.js/1.0.6/wordcloud2.min.js",
        "https://raw.githubusercontent.com/timdream/wordcloud2.js/gh-pages/src/wordcloud2.js",

    ]
myEnum = "circle", "cartoid", "diamond", "square", "triangle-forward", "triangle", "pentagon", "star"


class WordCloud2(_WordCloud2Meta):
    """
    Provides a Bokeh Interface to WordCloud  (https://wordcloud2-js.timdream.org)

    As Such it accepts Most of the same arguments.

    .. note::

       - any CustomJS callback will have two variables available `cb_obj` which is the model, and `cb_data` which is the data for the CustomJS Callback
       - depending on context `cb_data` will have different properties, but *usually* `cb_data.word` and `cb_data.weight` will be available
       - many CustomJS callbacks **MUST** return a value (see the docs for the various attributes)

    """
    source = Instance(DataSource, help="""
        **required** The source of data for the widget.
        
        .. code-block:: python
        
           data = ColumnDataSource(data=dict(words=list("ABCDE"),sizes=[1,4,2,5,7]))
           WordCloud(source=data, wordCol="words", sizeCol="sizes", color="blue")
        
        """)

    view = Instance(CDSView, help="""
        A view into the data source to use when rendering table rows. A default view
        of the entire data source is created if a view is not passed in during
        initialization.
        
        .. code-block:: python
        
           view = CDSView(source=data,filter=GroupFilter(column_name="active",value="true"))        
           WordCloud(source=data, view=view, wordCol="words", sizeCol="sizes", color=["red","blue"])
                                         
        """)

    sizeCol = String(help="the column of the weights, if unspecified it will count word occurences")
    wordCol = String(help="**required** the column with the words in it")
    color = Either(String,List(String),Instance(CustomJS),help="""
     the color or colors to use when generating the wordcloud
     
     .. code-block:: python
     
         data = ColumnDataSource(data={
            words = ['apple','pie','tastes','delicious'],
            weights = [11,10,20,15],
            colors=['red','blue','blue','green']
         })
         
         # a single color, all words will be pink on a blue background
         wc1 = WordCloud(source=data,wordCol="words", sizeCol="weights", color="pink", background="blue")
         
         # 2 colors that will be selected at random, on a yellow background
         wc2 = WordCloud(source=data,wordCol="words", sizeCol="weights", background="yellow",color=["blue","red"])
         
         # specify a column to use for the colors
         wc3 = WordCloud(source=data,wordCol="words", sizeCol="weights", background="yellow",color="colors")
         
         # specify a javascript callback ,(default white background)
         callback = CustomJS(code='''
         if cb_data.word == 'apple':
            return 'red'
         return 'blue'
         ''')
         wc4 = WordCloud(source=data,wordCol="words", sizeCol="weights", color=callback)
         
    """)
    fontWeight = Either(String,Instance(CustomJS),default="normal",help="the font weight to use, or a CustomJS that returns a Font weight(eg. 'bolder','600','normal') (see `cb_object`)")
    classes = Either(String,Instance(CustomJS),help="a class name or function to use ... only works if using DOM elements, which are currently unsupported... so this does nothing for now")
    weightFactor = Either(Instance(CustomJS),Float,help="""
    a multiplier to apply to the sizes or a CustomJS instance(see `cb_data`)
    
    .. code-block:: python
    
       # you can just specify a number (eg multiply all sizes by 12)
       wc = WordCloud(source=data,wordCol="words", sizeCol="weights", weightFactor=12)
       
       # or you can specify a callback (eg cube the given size)
       callback = CustomJS(code="return Math.pow(cb_data.size, 3))
       
    """)

    rotateRatio = Float(help="the odds of a given word rotating between 0-1, if 1 then the word will ALWAYS rotate, if 0 it will NEVER rotate, at 0.2 it has a 20% chance of rotating",default=1)
    minRotation = Float(help="the minimum amount(in radians) to rotate",default=0)
    maxRotation = Float(help="the maximum amount(in radians) to rotate",default=math.pi/2.0)
    rotationSteps = Int(help="the number of slices to cut the rotation range into",default=32)
    gridSize = Float(help="the distance between words, the bigger the gridsize, the more distance between words.",default=16)
    fontFamily = String(help="the fontFamily to use.",default="Times, serif")
    shape = Enum(*myEnum, help="the shape of the wordcloud",default="square")

    hover = Instance(CustomJS,help="""
    js callback to execute on word hover 1
    
    `cb_data` provides: `cb_data.word`, and `cb_data.weight`
    
    .. code-block:: python
    
       wordcloud.hover = CustomJS(code="console.log(`Hover On: ${cb_data.word} - x${cb_data.weight}`)")
    
  
    """)
    click = Instance(CustomJS,help="""
    js callback to execute on word click
    
    .. note::
    
       this is **NOT** the same as :meth:`bokeh_wordcloud2.WordCloud2.on_click`, which runs inside the backend on a
       bokeh server, where as this attribute expects `CustomJS` that is run on the client.
    
    
    `cb_data` provides: `cb_data.word`, and `cb_data.weight`
    
    .. code-block:: python
    
       wordcloud.click = CustomJS(code='''
       console.log(`You Clicked!!!!: ${cb_data.word} - x${cb_data.weight}`)
       ''')
       
    """)

    def __init__(self, **kw):
        super(WordCloud2, self).__init__(**kw)
        if "view" not in kw:
            self.view = CDSView(source=self.source)
    def on_click(self,python_callback):
        """
        bind a python callback to word clicks, this only works when running a bokeh server

        .. note::

           this is **NOT** the same as :attr:`bokeh_wordcloud2.WordCloud2.click`, which runs on the clients browser,
           where as this method expects a python function that is run on the bokeh-server.

        the function that recieves the call back will recieve  WordClick Event, that has a word and weight attribute

        .. code-block:: python

           def my_handler(event):
               print("Clicked Word: %r"%event.word)
               # update the view filters
               some_view.filters = [1,2,4,5,7,8]

           wordcloud.on_click(my_handler)

        :param python_callback: a python function to call when a word is clicked
        """
        self.on_event(WordClick, python_callback)



