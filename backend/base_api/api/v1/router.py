from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from base_api.api.v1.users.router_auth import router as router_auth
from base_api.api.v1.users.router_users import router as router_users
from base_api.api.v1.runs.router import router as router_runs
from base_api.api.v1.races.router import router as router_races
from base_api.api.v1.course_elements.router import router as router_course_elements
from base_api.api.v1.gates.router import router as router_gates
from base_api.api.v1.splits.router import router as router_splits
from base_api.api.v1.starts.router import router as router_starts
from base_api.api.v1.finishes.router import router as router_finishes


from base_api.api.v1.competition_owners.router import (
    router as router_competition_owners,
)
from base_api.api.v1.finish_runs.router import router as router_finish_runs
from base_api.api.v1.race_registrations.router import (
    router as router_race_registrations,
)
from base_api.api.v1.split_runs.router import router as router_split_runs
from base_api.api.v1.competitor_medal_groups.router import (
    router as router_competitor_medal_groups,
)
from base_api.api.v1.competitions.router import router as router_competitions
from base_api.api.v1.agg_race_results.router import router as router_agg_race_results
from base_api.api.v1.competition_scoring_rules.router import (
    router as router_competition_scoring_rules,
)
from base_api.api.v1.start_runs.router import router as router_start_runs
from base_api.api.v1.competitor_runs.router import router as router_competitor_runs
from base_api.api.v1.competitors.router import router as router_competitors
from base_api.api.v1.competition_results.router import (
    router as router_competition_results,
)
from base_api.api.v1.race_stages.router import router as router_race_stages
from base_api.api.v1.bib_competitors.router import router as router_bib_competitors
from base_api.api.v1.bib_athletes.router import router as router_bib_athletes
from base_api.api.v1.competition_registered_users.router import (
    router as router_competition_registered_users,
)
from base_api.api.v1.gate_runs.router import router as router_gate_runs
from base_api.api.v1.judgement_groups.router import router as router_judgement_groups
from base_api.api.v1.medal_groups.router import router as router_medal_groups
from base_api.api.v1.bibs.router import router as router_bibs
from base_api.api.v1.race_classes.router import router as router_race_classes
from base_api.api.v1.agg_run_results.router import router as router_agg_run_results
from base_api.api.v1.athletes.router import router as router_athletes
from base_api.api.v1.user_profiles.router import router as router_user_profiles
from base_api.api.v1.scoring_rules.router import router as router_scoring_rules

# from base_api.api.v1.router_websocket import router as router_websocket
from core.config import settings

http_bearer = HTTPBearer(auto_error=False)


router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)
# router.include_router(router_user)
# router.include_router(router_competition)
# router.include_router(router_websocket)
router.include_router(router_auth)
router.include_router(router_users)
router.include_router(router_runs)
router.include_router(router_races)
router.include_router(router_course_elements)
router.include_router(router_gates)
router.include_router(router_splits)
router.include_router(router_starts)
router.include_router(router_finishes)


router.include_router(router_judgement_groups)
router.include_router(router_athletes)
router.include_router(router_competition_registered_users)
router.include_router(router_race_classes)
router.include_router(router_gate_runs)
router.include_router(router_competition_scoring_rules)
router.include_router(router_competitions)
router.include_router(router_user_profiles)
router.include_router(router_start_runs)
router.include_router(router_competitor_medal_groups)
router.include_router(router_agg_race_results)
router.include_router(router_race_registrations)
router.include_router(router_bib_athletes)
router.include_router(router_bib_competitors)
router.include_router(router_split_runs)
router.include_router(router_competitor_runs)
router.include_router(router_agg_run_results)
router.include_router(router_finish_runs)
router.include_router(router_bibs)
router.include_router(router_medal_groups)
router.include_router(router_competition_results)
router.include_router(router_competitors)
router.include_router(router_competition_owners)
router.include_router(router_race_stages)
router.include_router(router_scoring_rules)
