#!/usr/bin/env bash
readonly SCRIPT_DIRECTORY=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd);
readonly ENV_NAME=skoolcar_env
readonly PROJECT_DIRECTORY=${SCRIPT_DIRECTORY}/..

function main
{
    echo "Install development environment.";

    set -o errexit
    set -o pipefail
    set -o nounset
    set -o errtrace

    install_dev_env;
}

function install_dev_env
{
    # Create environment with dev dependencies
    echo "Install dependencies."
    conda env create -q -f ${PROJECT_DIRECTORY}/env_management/environment_rpi.yml -n ${ENV_NAME}
    echo "Done."
}

main