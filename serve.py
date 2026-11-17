# SPDX-License-Identifier: Apache-2.0

"""Entry point: the WebSocket server the PLE evaluator connects to on $PORT.

All agent logic lives in `harness.py`; this file only starts the serve-protocol
server (`taskbridge.run`) and hands each task session to `harness.solve`.
"""

import harness
import taskbridge

if __name__ == "__main__":
  taskbridge.run(harness.solve)
