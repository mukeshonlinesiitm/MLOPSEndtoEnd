from zenml import pipeline

from steps.etl import get_or_create_user,crawl_links


@pipeline
def digital_data_etl(user_full_name: str, links: list[str]) -> str:
    user = get_or_create_user(user_full_name)
    last_step = crawl_links(user=user, links=links)
    return last_step.invocation_id
