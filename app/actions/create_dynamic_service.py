from cookiecutter.main import cookiecutter

from actions.base_create_service import BaseCreateService
from utils import get_unique_output_dir
from core.config import settings

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CreateDynamicService(BaseCreateService):

    def _create_cookiecutter(self, props: dict):
        cookiecutter_template_url = props.pop('cookiecutter_url')
        logger.info(f"using {cookiecutter_template_url} as the cookiecutter template")
        return cookiecutter(cookiecutter_template_url, extra_context=props,
                            no_input=True, output_dir=get_unique_output_dir())
