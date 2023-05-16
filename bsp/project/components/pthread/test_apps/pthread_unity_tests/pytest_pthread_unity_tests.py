# SPDX-FileCopyrightText: 2022 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

from time import sleep

import pytest
from pytest_embedded import Dut


@pytest.mark.generic
@pytest.mark.supported_targets
@pytest.mark.parametrize(
    'config',
    [
        'default',
    ],
    indirect=True,
)
def test_pthread(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('![thread-specific]')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        pytest.param('single_core_esp32', marks=[pytest.mark.esp32]),
        pytest.param('single_core_esp32s3', marks=[pytest.mark.esp32s3]),
    ],
    indirect=True,
)
def test_pthread_single_core(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('![thread-specific]')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.generic
@pytest.mark.supported_targets
@pytest.mark.parametrize(
    'config',
    [
        'tls',
    ],
    indirect=True,
)
def test_pthread_tls(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('[thread-specific]')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.generic
@pytest.mark.parametrize(
    'config',
    [
        pytest.param('single_core_esp32_tls', marks=[pytest.mark.esp32]),
    ],
    indirect=True,
)
def test_pthread_single_core_tls(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    dut.write('[thread-specific]')
    dut.expect_unity_test_output(timeout=300)


@pytest.mark.qemu
@pytest.mark.esp32
def test_pthread_qemu(dut: Dut) -> None:
    dut.expect_exact('Press ENTER to see the list of tests')
    # dut may not be ready to accept input, so adding the delay until handled in pytest embedded (RDT-328)
    sleep(1)
    dut.write('![qemu-ignore]')
    dut.expect_unity_test_output(timeout=300)
