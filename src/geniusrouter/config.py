from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


class ConfigError(ValueError):
    """Raised when GeniusRouter configuration is missing or invalid."""


@dataclass(frozen=True)
class RoutingConfig:
    low_iq: str
    medium_iq: str
    high_iq: str


@dataclass(frozen=True)
class LocalRigsConfig:
    low_url: str = ""
    medium_url: str = ""
    high_url: str = ""


@dataclass(frozen=True)
class ClassifierConfig:
    model: str
    enabled: bool = True


@dataclass(frozen=True)
class CacheConfig:
    enabled: bool = True
    ttl_seconds: int = 3600


@dataclass(frozen=True)
class GeniusRouterConfig:
    routing: RoutingConfig
    local_rigs: LocalRigsConfig
    classifier: ClassifierConfig
    cache: CacheConfig
    config_version: str = "GeniusRouter-SA-v0.2"


def _section(data: dict[str, Any], name: str) -> dict[str, Any]:
    section = data.get(name)
    if not isinstance(section, dict):
        raise ConfigError(f"Missing or invalid config section: {name}")
    return section


def _required_str(section: dict[str, Any], key: str, section_name: str) -> str:
    value = section.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Missing or invalid string: {section_name}.{key}")
    return value.strip()


def validate_config(data: dict[str, Any]) -> GeniusRouterConfig:
    if not isinstance(data, dict):
        raise ConfigError("Config root must be a mapping")

    routing = _section(data, "routing")
    local_rigs = data.get("local_rigs") or {}
    classifier = data.get("classifier") or {}
    cache = data.get("cache") or {}

    if not isinstance(local_rigs, dict):
        raise ConfigError("local_rigs must be a mapping")
    if not isinstance(classifier, dict):
        raise ConfigError("classifier must be a mapping")
    if not isinstance(cache, dict):
        raise ConfigError("cache must be a mapping")

    cache_ttl = int(cache.get("ttl_seconds", 3600))
    if cache_ttl <= 0:
        raise ConfigError("cache.ttl_seconds must be positive")

    return GeniusRouterConfig(
        routing=RoutingConfig(
            low_iq=_required_str(routing, "low_iq", "routing"),
            medium_iq=_required_str(routing, "medium_iq", "routing"),
            high_iq=_required_str(routing, "high_iq", "routing"),
        ),
        local_rigs=LocalRigsConfig(
            low_url=str(local_rigs.get("low_url", "") or ""),
            medium_url=str(local_rigs.get("medium_url", "") or ""),
            high_url=str(local_rigs.get("high_url", "") or ""),
        ),
        classifier=ClassifierConfig(
            model=str(classifier.get("model", "granite4:350m") or "granite4:350m"),
            enabled=bool(classifier.get("enabled", True)),
        ),
        cache=CacheConfig(
            enabled=bool(cache.get("enabled", True)),
            ttl_seconds=cache_ttl,
        ),
    )


def load_config(path: str | Path = "config.yaml") -> GeniusRouterConfig:
    try:
        import yaml
    except Exception as exc:
        raise ConfigError("PyYAML is required to load config.yaml") from exc

    config_path = Path(path)
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    return validate_config(data)