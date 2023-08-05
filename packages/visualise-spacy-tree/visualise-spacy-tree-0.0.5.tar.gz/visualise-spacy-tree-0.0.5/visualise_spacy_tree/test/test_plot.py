import os
import en_core_web_sm
from spacy.tokens import Token
import visualise_spacy_tree

text = 'Forging involves the shaping of metal using localized compressive forces.'

nlp = en_core_web_sm.load()
doc = nlp(text)

example_plot_dir = 'visualise_spacy_tree/example_plots/'


def test_default_plot():
    plot = visualise_spacy_tree.create_png(doc)
    with open(os.path.join(example_plot_dir, 'default_plot.png'), 'wb') as f:
        f.write(plot)


def test_custom_plot():
    Token.set_extension('plot', default={'color': 'aquamarine'})
    for token in doc:
        node_text = '{0} [{1}]\n({2} / {3})'.format(
                token.orth_,
                token.i,
                token.pos_,
                token.tag_
            )
        token._.plot['text'] = node_text
        if token.dep_ in ['ROOT', 'acl']:
            token._.plot['color'] = 'dodgerblue'
        if token.dep_ in ['nsubj', 'dobj']:
            token._.plot['color'] = 'deeppink1'
    plot = visualise_spacy_tree.create_png(doc)
    with open(os.path.join(example_plot_dir, 'custom_plot.png'), 'wb') as f:
        f.write(plot)


def test_partial_plot():
    tokens = [doc[0], doc[1], doc[3]]
    plot = visualise_spacy_tree.create_png(tokens)
    with open(os.path.join(example_plot_dir, 'default_partial_plot.png'), 'wb') as f:
        f.write(plot)


