import spacy
from pprint import pprint
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from pyvis.network import Network
from backend.rebel.rebel_inference import from_text_to_kb


def get_loaded_model_dict():
    '''
    Loading all the models.
    This function should be called just once in the main script
    '''
    loaded_model_dict = {
        'sentence_model': None,
        'rebel_model': None,
        'rebel_tokenizer': None
    }
    # sentence splittin_model
    try:
        loaded_model_dict['sentence_model'] = spacy.load('en_core_web_sm')
        print('\n')
        print('Sentence model loaded ')
        print('\n')
    except Exception as e:
        print(e)
        print('Sentence model not loaded properly')
    
    # rebel model
    try:
        loaded_model_dict['rebel_tokenizer'] = AutoTokenizer.from_pretrained("Babelscape/rebel-large")
        loaded_model_dict['rebel_model'] = AutoModelForSeq2SeqLM.from_pretrained("Babelscape/rebel-large")
        print('\n')
        print('Rebel model and tokenizer loaded successfully')
        print('\n')
    except Exception as e:
        print(e)
        print('Rebel model and tokenizer did not loaded successfully')

    return loaded_model_dict


def save_network_html(kb, filename="network.html"):
    # create network
    net = Network(directed=True, width="700px", height="700px", bgcolor="#eeeeee")

    # nodes
    color_entity = "#00FF00"
    for e in kb.entities:
        net.add_node(e, shape="circle", color=color_entity)

    # edges
    for r in kb.relations:
        net.add_edge(r["head"], r["tail"],
                    title=r["type"], label=r["type"])
        
    # save network
    net.repulsion(
        node_distance=200,
        central_gravity=0.2,
        spring_length=200,
        spring_strength=0.05,
        damping=0.09
    )
    net.set_edge_smooth('dynamic')
    # net.show(filename)
    net.save_graph(filename)
    return


def get_triples(text, model_dict):
    kb = from_text_to_kb(
        model_dict['rebel_model'], model_dict['rebel_tokenizer'],
        text, span_length=64, verbose=True
    )
    return kb



if __name__ == "__main__":
    model_dict = get_loaded_model_dict()
    text = "Mohandas Karamchand Gandhi was an Indian lawyer, anti-colonial nationalist and political ethicist[6] who employed nonviolent resistance to lead the successful campaign for India independence from British rule and to later inspire movements for civil rights and freedom across the world. The honorific Mahātmā, first applied to him in 1914 in South Africa, is now used throughout the world. Born and raised in a Hindu family in coastal Gujarat, Gandhi trained in the law at the Inner Temple, London, and was called to the bar at age 22 in June 1891. After two uncertain years in India, where he was unable to start a successful law practice, he moved to South Africa in 1893 to represent an Indian merchant in a lawsuit. He went on to live in South Africa for 21 years. It was here that Gandhi raised a family and first employed nonviolent resistance in a campaign for civil rights. In 1915, aged 45, he returned to India and soon set about organising peasants, farmers, and urban labourers to protest against excessive land-tax and discrimination.Assuming leadership of the Indian National Congress in 1921, Gandhi led nationwide campaigns for easing poverty, expanding women rights, building religious and ethnic amity, ending untouchability, and, above all, achieving swaraj or self-rule. Gandhi adopted the short dhoti woven with hand-spun yarn as a mark of identification with India's rural poor. He began to live in a self-sufficient residential community, to eat simple food, and undertake long fasts as a means of both introspection and political protest. Bringing anti-colonial nationalism to the common Indians, Gandhi led them in challenging the British-imposed salt tax with the 400 km (250 mi) Dandi Salt March in 1930 and in calling for the British to quit India in 1942. He was imprisoned many times and for many years in both South Africa and India."
    kb = get_triples(text, model_dict)
    filename = "sample_network.html"
    save_network_html(kb, filename=filename)