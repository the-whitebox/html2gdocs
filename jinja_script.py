from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))


# Your data dictionary
data = {
    "id": "123",
    "domain": "aaa",
    "topic": "aaa",
    "db": "us",
    "latest-step": "aaa",
    "primary_keywords_0_keyword": "bbb",
    "primary_keywords_0_intent": "aaa",
    "primary_keywords_0_search_volume": 123,
    "primary_keywords_0_source": "semrush",
    "primary_keywords_0_active": True,
    "primary_keywords_0_urls_0_link": "a1234sfa",
    "primary_keywords_0_urls_0_backlinks": 123,
    "primary_keywords_0_urls_0_entities_0_entity": "aaa",
    "primary_keywords_0_urls_0_entities_0_saliency_score": 123,
    "primary_keywords_0_urls_0_intents_0": "aaa",
    "primary_keywords_0_urls_0_intents_1": "bbb",
    "primary_keywords_0_PAA_0_question": "aaa",
    "primary_keywords_0_PAA_0_answer": "aaa",
    "primary_keywords_0_PAA_0_link": "a1234sfa",
    "primary_keywords_0_carousel_0_title": "aaa",
    "primary_keywords_0_carousel_0_link": "a1234sfa",
    "primary_keywords_0_featured_snippet_0_answer": "aaa",
    "primary_keywords_0_featured_snippet_0_link": "a1234sfa",
    "secondary_keywords_0_keyword": "bbb",
    "secondary_keywords_0_intent": "aaa",
    "secondary_keywords_0_search_volume": 123,
    "secondary_keywords_0_source": "semrush",
    "secondary_keywords_0_active": True,
    "secondary_keywords_0_urls_0_link": "a1234sfa",
    "secondary_keywords_0_urls_0_backlinks": 123,
    "secondary_keywords_0_urls_0_entities_0_entity": "aaa",
    "secondary_keywords_0_urls_0_entities_0_saliency_score": 123,
    "secondary_keywords_0_urls_0_intents_0": "aaa",
    "secondary_keywords_0_urls_0_intents_1": "bbb",
    "secondary_keywords_0_PAA_0_question": "aaa",
    "secondary_keywords_0_PAA_0_answer": "aaa",
    "secondary_keywords_0_PAA_0_link": "a1234sfa",
    "secondary_keywords_0_carousel_0_title": "aaa",
    "secondary_keywords_0_carousel_0_link": "a1234sfa",
    "secondary_keywords_0_featured_snippet_0_answer": "aaa",
    "secondary_keywords_0_featured_snippet_0_link": "a1234sfa",
    "content_template_page_title": "aaa",
    "content_template_h1_tag": "abcd",
    "content_template_opening_content": "abcd",
    "content_template_h2_tags_0": "abcd",
    "content_template_h3_tags_0": "abcd",
    "content_template_h4_tags_0": "abcd",
    "content_template_h5_tags_0": "abcd",
    "content_template_h6_tags_0": "abcd",
    "content_template_meta_description": "aaa",
    "content_template_page_structure": "?",
    "content_template_entities_0": "abcd",
    "content_template_entities_1": "efgh",
    "content_template_min_word_count": 123,
    "content_template_schema_markups": "?",
    "content_template_FAQ_0": "aaa",
    "content_template_FAQ_1": "bbb",
    "breadcrumbs_0": "1-aaa",
    "breadcrumbs_1": "2-bbb",
    "final_url": "aaa123.com/bbb",
    "category": "aaa",
    "internal_links_0_target_url": "aaa123.com/bbb",
    "internal_links_0_anchor_text": "aaa"
}


# Load the template file
template = env.get_template('index.html')

# Render the template with the data
rendered_html = template.render(data=data)
print(rendered_html)

# Save the rendered HTML to a file
# with open('output.html', 'w') as file:
#     file.write(rendered_html)
