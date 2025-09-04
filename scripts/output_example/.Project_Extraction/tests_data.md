<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: tests\data - Current Tree Structure
```
📂 data
├─ 🔧 baseline.json (197 lines)
├─ 🔧 pr-baseline.json (197 lines)
├─ 🔧 pr-results.json (0 lines)
├─ 🔧 results.json (197 lines)
└─ 🔧 stress-results.json (97 lines)
```

## 📄 Project File Contents


=== File: tests\data\baseline.json (197 lines) ===

```json
{
  "config_loading": {
    "speed_ms": 0.38,
    "memory_mb": 81.92,
    "memory_delta_mb": 77.14,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:27.092Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": 0.23,
      "baseline_speed_ms": 0.38,
      "baseline_memory_mb": 81.73
    }
  },
  "constants_access": {
    "speed_ms": 0.03,
    "memory_mb": 69.6,
    "memory_delta_mb": -12.33,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:29.764Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": 0.26,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 69.42
    }
  },
  "client_initialization": {
    "speed_ms": 0.65,
    "memory_mb": 214.05,
    "memory_delta_mb": 144.44,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:37.124Z",
    "baseline_comparison": {
      "speed_change_percent": -1.52,
      "memory_change_percent": -0.34,
      "baseline_speed_ms": 0.66,
      "baseline_memory_mb": 214.78
    }
  },
  "shutdown_preparation": {
    "speed_ms": 0.03,
    "memory_mb": 204.15,
    "memory_delta_mb": -9.91,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:37.769Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": -0.41,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 205
    }
  },
  "real_db_init": {
    "speed_ms": 0.85,
    "memory_mb": 215.62,
    "memory_delta_mb": 11.44,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:38.626Z",
    "baseline_comparison": {
      "speed_change_percent": -1.16,
      "memory_change_percent": -0.33,
      "baseline_speed_ms": 0.86,
      "baseline_memory_mb": 216.33
    }
  },
  "real_db_operations": {
    "speed_ms": 8.47,
    "memory_mb": 195.46,
    "memory_delta_mb": -20.16,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:55.693Z",
    "baseline_comparison": {
      "speed_change_percent": 8.17,
      "memory_change_percent": -0.21,
      "baseline_speed_ms": 7.83,
      "baseline_memory_mb": 195.88
    }
  },
  "permission_check": {
    "speed_ms": 0,
    "memory_mb": 196.78,
    "memory_delta_mb": 1.29,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:55.702Z",
    "baseline_comparison": {
      "speed_change_percent": null,
      "memory_change_percent": 0.32,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.15
    }
  },
  "admin_permission_check": {
    "speed_ms": 0,
    "memory_mb": 196.79,
    "memory_delta_mb": 0,
    "status": "pass",
    "timestamp": "2025-09-03T20:26:55.707Z",
    "baseline_comparison": {
      "speed_change_percent": null,
      "memory_change_percent": 0.73,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 195.36
    }
  },
  "rate_limit_check": {
    "speed_ms": 6.59,
    "memory_mb": 197.85,
    "memory_delta_mb": 1.01,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.256Z",
    "baseline_comparison": {
      "speed_change_percent": 13.62,
      "memory_change_percent": -0.41,
      "baseline_speed_ms": 5.8,
      "baseline_memory_mb": 198.67
    }
  },
  "rate_limit_cleanup": {
    "speed_ms": 0.17,
    "memory_mb": 198.79,
    "memory_delta_mb": 0.92,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.605Z",
    "baseline_comparison": {
      "speed_change_percent": 6.25,
      "memory_change_percent": 0.37,
      "baseline_speed_ms": 0.16,
      "baseline_memory_mb": 198.06
    }
  },
  "command_parsing": {
    "speed_ms": 0,
    "memory_mb": 204.46,
    "memory_delta_mb": 7.23,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.678Z",
    "baseline_comparison": {
      "speed_change_percent": null,
      "memory_change_percent": -0.36,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 205.2
    }
  },
  "plugin_loading": {
    "speed_ms": 0.04,
    "memory_mb": 203.65,
    "memory_delta_mb": -0.81,
    "status": "pass",
    "timestamp": "2025-09-03T20:28:02.899Z",
    "baseline_comparison": {
      "speed_change_percent": -20,
      "memory_change_percent": -0.35,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 204.37
    }
  },
  "audit_logging": {
    "speed_ms": 185.89,
    "memory_mb": 203.58,
    "memory_delta_mb": -0.08,
    "status": "pass",
    "timestamp": "2025-09-03T20:29:34.578Z",
    "baseline_comparison": {
      "speed_change_percent": 11.73,
      "memory_change_percent": 0.03,
      "baseline_speed_ms": 166.37,
      "baseline_memory_mb": 203.51
    }
  },
  "api_server_lifecycle": {
    "speed_ms": 0.05,
    "memory_mb": 203.16,
    "memory_delta_mb": -0.43,
    "status": "pass",
    "timestamp": "2025-09-03T20:29:34.633Z",
    "baseline_comparison": {
      "speed_change_percent": 0,
      "memory_change_percent": 0.04,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 203.07
    }
  },
  "docs_generation": {
    "speed_ms": 20.81,
    "memory_mb": 200.8,
    "memory_delta_mb": -2.37,
    "status": "pass",
    "timestamp": "2025-09-03T20:29:45.401Z",
    "baseline_comparison": {
      "speed_change_percent": -0.14,
      "memory_change_percent": -1.95,
      "baseline_speed_ms": 20.84,
      "baseline_memory_mb": 204.8
    }
  }
}
```

=== File: tests\data\pr-baseline.json (197 lines) ===

```json
{
  "config_loading": {
    "speed_ms": 0.28,
    "memory_mb": 78.41,
    "memory_delta_mb": 75.02,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:25.808Z",
    "baseline_comparison": {
      "speed_change_ms": -0.1,
      "memory_change_mb": -3.51,
      "baseline_speed_ms": 0.38,
      "baseline_memory_mb": 81.92
    }
  },
  "constants_access": {
    "speed_ms": 0.03,
    "memory_mb": 78.43,
    "memory_delta_mb": 0.03,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:29.145Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 8.83,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 69.6
    }
  },
  "client_initialization": {
    "speed_ms": 0.33,
    "memory_mb": 249.97,
    "memory_delta_mb": 171.54,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:33.021Z",
    "baseline_comparison": {
      "speed_change_ms": -0.32,
      "memory_change_mb": 35.92,
      "baseline_speed_ms": 0.65,
      "baseline_memory_mb": 214.05
    }
  },
  "shutdown_preparation": {
    "speed_ms": 0.04,
    "memory_mb": 249.87,
    "memory_delta_mb": -0.02,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:34.041Z",
    "baseline_comparison": {
      "speed_change_ms": 0.01,
      "memory_change_mb": 45.72,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 204.15
    }
  },
  "real_db_init": {
    "speed_ms": 0.48,
    "memory_mb": 250.01,
    "memory_delta_mb": 0.15,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:34.810Z",
    "baseline_comparison": {
      "speed_change_ms": -0.37,
      "memory_change_mb": 34.39,
      "baseline_speed_ms": 0.85,
      "baseline_memory_mb": 215.62
    }
  },
  "real_db_operations": {
    "speed_ms": 2.18,
    "memory_mb": 250.18,
    "memory_delta_mb": -0.06,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:39.521Z",
    "baseline_comparison": {
      "speed_change_ms": -6.29,
      "memory_change_mb": 54.72,
      "baseline_speed_ms": 8.47,
      "baseline_memory_mb": 195.46
    }
  },
  "permission_check": {
    "speed_ms": 0,
    "memory_mb": 250.17,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:39.779Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 53.39,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.78
    }
  },
  "admin_permission_check": {
    "speed_ms": 0,
    "memory_mb": 250.17,
    "memory_delta_mb": 0,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:40.035Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 53.38,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.79
    }
  },
  "rate_limit_check": {
    "speed_ms": 1.57,
    "memory_mb": 250.26,
    "memory_delta_mb": 0.08,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:55.886Z",
    "baseline_comparison": {
      "speed_change_ms": -5.02,
      "memory_change_mb": 52.41,
      "baseline_speed_ms": 6.59,
      "baseline_memory_mb": 197.85
    }
  },
  "rate_limit_cleanup": {
    "speed_ms": 0.14,
    "memory_mb": 250.26,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:56.392Z",
    "baseline_comparison": {
      "speed_change_ms": -0.03,
      "memory_change_mb": 51.47,
      "baseline_speed_ms": 0.17,
      "baseline_memory_mb": 198.79
    }
  },
  "command_parsing": {
    "speed_ms": 0,
    "memory_mb": 250.28,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:56.691Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 45.82,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 204.46
    }
  },
  "plugin_loading": {
    "speed_ms": 0.01,
    "memory_mb": 250.32,
    "memory_delta_mb": 0.04,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:56.980Z",
    "baseline_comparison": {
      "speed_change_ms": -0.03,
      "memory_change_mb": 46.67,
      "baseline_speed_ms": 0.04,
      "baseline_memory_mb": 203.65
    }
  },
  "audit_logging": {
    "speed_ms": 2.14,
    "memory_mb": 250.37,
    "memory_delta_mb": 0.06,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:58.328Z",
    "baseline_comparison": {
      "speed_change_ms": -183.75,
      "memory_change_mb": 46.79,
      "baseline_speed_ms": 185.89,
      "baseline_memory_mb": 203.58
    }
  },
  "api_server_lifecycle": {
    "speed_ms": 0.01,
    "memory_mb": 250.38,
    "memory_delta_mb": 0.01,
    "status": "pass",
    "timestamp": "2025-09-03T21:39:58.586Z",
    "baseline_comparison": {
      "speed_change_ms": -0.04,
      "memory_change_mb": 47.22,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 203.16
    }
  },
  "docs_generation": {
    "speed_ms": 17.78,
    "memory_mb": 253.54,
    "memory_delta_mb": 3.16,
    "status": "pass",
    "timestamp": "2025-09-03T21:40:07.935Z",
    "baseline_comparison": {
      "speed_change_ms": -3.03,
      "memory_change_mb": 52.74,
      "baseline_speed_ms": 20.81,
      "baseline_memory_mb": 200.8
    }
  }
}
```

=== File: tests\data\pr-results.json (0 lines) ===

```json

```

=== File: tests\data\results.json (197 lines) ===

```json
{
  "config_loading": {
    "speed_ms": 0.38,
    "memory_mb": 75.23,
    "memory_delta_mb": 70.45,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:17.286Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -6.69,
      "baseline_speed_ms": 0.38,
      "baseline_memory_mb": 81.92
    }
  },
  "constants_access": {
    "speed_ms": 0.03,
    "memory_mb": 77.51,
    "memory_delta_mb": 2.26,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:19.977Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 7.91,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 69.6
    }
  },
  "client_initialization": {
    "speed_ms": 0.67,
    "memory_mb": 206.91,
    "memory_delta_mb": 129.4,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:27.515Z",
    "baseline_comparison": {
      "speed_change_ms": 0.02,
      "memory_change_mb": -7.14,
      "baseline_speed_ms": 0.65,
      "baseline_memory_mb": 214.05
    }
  },
  "shutdown_preparation": {
    "speed_ms": 0.03,
    "memory_mb": 210.74,
    "memory_delta_mb": 3.81,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:28.165Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 6.59,
      "baseline_speed_ms": 0.03,
      "baseline_memory_mb": 204.15
    }
  },
  "real_db_init": {
    "speed_ms": 0.9,
    "memory_mb": 209.21,
    "memory_delta_mb": -1.56,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:29.054Z",
    "baseline_comparison": {
      "speed_change_ms": 0.05,
      "memory_change_mb": -6.41,
      "baseline_speed_ms": 0.85,
      "baseline_memory_mb": 215.62
    }
  },
  "real_db_operations": {
    "speed_ms": 8.55,
    "memory_mb": 196.16,
    "memory_delta_mb": -13.05,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:46.097Z",
    "baseline_comparison": {
      "speed_change_ms": 0.08,
      "memory_change_mb": 0.7,
      "baseline_speed_ms": 8.47,
      "baseline_memory_mb": 195.46
    }
  },
  "permission_check": {
    "speed_ms": 0,
    "memory_mb": 195.38,
    "memory_delta_mb": -0.81,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:46.105Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -1.4,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.78
    }
  },
  "admin_permission_check": {
    "speed_ms": 0,
    "memory_mb": 195.56,
    "memory_delta_mb": 0.18,
    "status": "pass",
    "timestamp": "2025-09-03T20:31:46.110Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -1.23,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 196.79
    }
  },
  "rate_limit_check": {
    "speed_ms": 6.59,
    "memory_mb": 196.71,
    "memory_delta_mb": 1.11,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:53.784Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": -1.14,
      "baseline_speed_ms": 6.59,
      "baseline_memory_mb": 197.85
    }
  },
  "rate_limit_cleanup": {
    "speed_ms": 0.2,
    "memory_mb": 197.7,
    "memory_delta_mb": 0.98,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:54.184Z",
    "baseline_comparison": {
      "speed_change_ms": 0.03,
      "memory_change_mb": -1.09,
      "baseline_speed_ms": 0.17,
      "baseline_memory_mb": 198.79
    }
  },
  "command_parsing": {
    "speed_ms": 0,
    "memory_mb": 204.78,
    "memory_delta_mb": 7.07,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:54.264Z",
    "baseline_comparison": {
      "speed_change_ms": 0,
      "memory_change_mb": 0.32,
      "baseline_speed_ms": 0,
      "baseline_memory_mb": 204.46
    }
  },
  "plugin_loading": {
    "speed_ms": 0.05,
    "memory_mb": 204.06,
    "memory_delta_mb": -0.72,
    "status": "pass",
    "timestamp": "2025-09-03T20:32:54.520Z",
    "baseline_comparison": {
      "speed_change_ms": 0.01,
      "memory_change_mb": 0.41,
      "baseline_speed_ms": 0.04,
      "baseline_memory_mb": 203.65
    }
  },
  "audit_logging": {
    "speed_ms": 184.05,
    "memory_mb": 202.41,
    "memory_delta_mb": -1.65,
    "status": "pass",
    "timestamp": "2025-09-03T20:34:27.066Z",
    "baseline_comparison": {
      "speed_change_ms": -1.84,
      "memory_change_mb": -1.17,
      "baseline_speed_ms": 185.89,
      "baseline_memory_mb": 203.58
    }
  },
  "api_server_lifecycle": {
    "speed_ms": 0.08,
    "memory_mb": 202.94,
    "memory_delta_mb": 0.53,
    "status": "pass",
    "timestamp": "2025-09-03T20:34:27.139Z",
    "baseline_comparison": {
      "speed_change_ms": 0.03,
      "memory_change_mb": -0.22,
      "baseline_speed_ms": 0.05,
      "baseline_memory_mb": 203.16
    }
  },
  "docs_generation": {
    "speed_ms": 24.96,
    "memory_mb": 202.86,
    "memory_delta_mb": -0.09,
    "status": "pass",
    "timestamp": "2025-09-03T20:34:40.117Z",
    "baseline_comparison": {
      "speed_change_ms": 4.15,
      "memory_change_mb": 2.06,
      "baseline_speed_ms": 20.81,
      "baseline_memory_mb": 200.8
    }
  }
}
```

=== File: tests\data\stress-results.json (97 lines) ===

```json
{
  "db_concurrent_writes": {
    "operations": 871,
    "errors": 0,
    "memoryStart": 21.08,
    "memoryPeak": 0,
    "opsPerSecond": 173.3098149327756,
    "errorRate": 0,
    "avgResponseTime": 57.646246039035546,
    "memoryGrowth": 2.360000000000003
  },
  "db_concurrent_reads": {
    "operations": 75,
    "errors": 0,
    "memoryStart": 23.44,
    "memoryPeak": 0,
    "opsPerSecond": 11.392985384470721,
    "errorRate": 0,
    "avgResponseTime": 1563.723512000001,
    "memoryGrowth": 44.07000000000001
  },
  "db_sustained_operations": {
    "operations": 399,
    "errors": 0,
    "memoryStart": 67.54,
    "opsPerSecond": 39.9,
    "errorRate": 0,
    "memoryGrowth": 8.429999999999993
  },
  "rate_limit_concurrent": {
    "operations": 391,
    "errors": 0,
    "memoryStart": 76.04,
    "memoryPeak": 0,
    "opsPerSecond": 128.76330518477474,
    "errorRate": 0,
    "avgResponseTime": 116.10876445012778,
    "memoryGrowth": -60.470000000000006
  },
  "permission_check_concurrent": {
    "operations": 6602749,
    "errors": 0,
    "memoryStart": 15.59,
    "memoryPeak": 0,
    "opsPerSecond": 3288785.1947138985,
    "errorRate": 0,
    "avgResponseTime": 0.01507224931618185,
    "memoryGrowth": 173.06
  },
  "rate_limit_boundaries": {
    "allowedCount": 10,
    "deniedCount": 10,
    "rateLimitWorking": true
  },
  "plugin_loading_concurrent": {
    "operations": 905923,
    "errors": 0,
    "memoryStart": 174.67,
    "memoryPeak": 0,
    "opsPerSecond": 452960.72996675957,
    "errorRate": 0,
    "avgResponseTime": 0.055048884066248235,
    "memoryGrowth": 43.400000000000006
  },
  "message_parsing_sustained": {
    "operations": 508,
    "errors": 0,
    "memoryStart": 218.07,
    "opsPerSecond": 63.5,
    "errorRate": 0,
    "memoryGrowth": -202.01999999999998
  },
  "api_lifecycle_concurrent": {
    "operations": 6682149,
    "errors": 0,
    "memoryStart": 16.08,
    "memoryPeak": 0,
    "opsPerSecond": 2227377.2830649717,
    "errorRate": 0,
    "avgResponseTime": 0.0021063294458101415,
    "memoryGrowth": 136.10000000000002
  },
  "memory_leak_detection": {
    "operations": 954,
    "errors": 0,
    "memoryStart": 152.19,
    "opsPerSecond": 63.6,
    "errorRate": 0,
    "memoryGrowth": -9.199999999999989
  },
  "memory_leak_analysis": {
    "initialMemory": 152.19,
    "finalMemory": 142.99,
    "potentialLeak": -9.199999999999989,
    "leakDetected": false
  }
}
```
