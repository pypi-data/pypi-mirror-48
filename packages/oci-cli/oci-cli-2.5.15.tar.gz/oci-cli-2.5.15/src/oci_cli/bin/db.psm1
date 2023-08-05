function GetOciTopLevelCommand_db() {
    return 'db'
}

function GetOciSubcommands_db() {
    $ociSubcommands = @{
        'db' = 'autonomous-container-database autonomous-data-warehouse autonomous-data-warehouse-backup autonomous-database autonomous-database-backup autonomous-exadata-infrastructure autonomous-exadata-infrastructure-shape backup data-guard-association database external-backup-job maintenance-run node patch patch-history system system-shape version'
        'db autonomous-container-database' = 'create get list restart terminate update'
        'db autonomous-data-warehouse' = 'create delete generate-wallet get list restore start stop update'
        'db autonomous-data-warehouse-backup' = 'create get list'
        'db autonomous-database' = 'create create-from-clone delete generate-wallet get list restore start stop update'
        'db autonomous-database-backup' = 'create get list'
        'db autonomous-exadata-infrastructure' = 'get launch list terminate update'
        'db autonomous-exadata-infrastructure-shape' = 'list'
        'db backup' = 'create delete get list'
        'db data-guard-association' = 'create failover get list reinstate switchover'
        'db data-guard-association create' = 'from-existing-db-system with-new-db-system'
        'db database' = 'create create-from-backup delete get list patch restore update'
        'db external-backup-job' = 'complete create get'
        'db maintenance-run' = 'get list update'
        'db node' = 'get list reset soft-reset start stop'
        'db patch' = 'get list'
        'db patch get' = 'by-database by-db-system'
        'db patch list' = 'by-database by-db-system'
        'db patch-history' = 'get list'
        'db patch-history get' = 'by-database by-db-system'
        'db patch-history list' = 'by-database by-db-system'
        'db system' = 'get get-exadata-iorm-config launch launch-from-backup list patch terminate update update-exadata-iorm-config'
        'db system-shape' = 'list'
        'db version' = 'list'
    }
    return $ociSubcommands
}

function GetOciCommandsToLongParams_db() {
    $ociCommandsToLongParams = @{
        'db autonomous-container-database create' = 'autonomous-exadata-infrastructure-id backup-config compartment-id defined-tags display-name freeform-tags from-json help max-wait-seconds patch-model service-level-agreement-type wait-for-state wait-interval-seconds'
        'db autonomous-container-database get' = 'autonomous-container-database-id from-json help'
        'db autonomous-container-database list' = 'all autonomous-exadata-infrastructure-id availability-domain compartment-id display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db autonomous-container-database restart' = 'autonomous-container-database-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-container-database terminate' = 'autonomous-container-database-id force from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-container-database update' = 'autonomous-container-database-id backup-config defined-tags display-name force freeform-tags from-json help if-match max-wait-seconds patch-model wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse create' = 'admin-password compartment-id cpu-core-count data-storage-size-in-tbs db-name defined-tags display-name freeform-tags from-json help license-model max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse delete' = 'autonomous-data-warehouse-id force from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse generate-wallet' = 'autonomous-data-warehouse-id file from-json help password'
        'db autonomous-data-warehouse get' = 'autonomous-data-warehouse-id from-json help'
        'db autonomous-data-warehouse list' = 'all compartment-id display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db autonomous-data-warehouse restore' = 'autonomous-data-warehouse-id from-json help if-match max-wait-seconds timestamp wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse start' = 'autonomous-data-warehouse-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse stop' = 'autonomous-data-warehouse-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse update' = 'admin-password autonomous-data-warehouse-id cpu-core-count data-storage-size-in-tbs defined-tags display-name force freeform-tags from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse-backup create' = 'autonomous-data-warehouse-id display-name from-json help max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-data-warehouse-backup get' = 'autonomous-data-warehouse-backup-id from-json help'
        'db autonomous-data-warehouse-backup list' = 'all autonomous-data-warehouse-id compartment-id display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db autonomous-database create' = 'admin-password autonomous-container-database-id compartment-id cpu-core-count data-storage-size-in-tbs db-name db-workload defined-tags display-name freeform-tags from-json help is-auto-scaling-enabled is-dedicated license-model max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-database create-from-clone' = 'admin-password autonomous-container-database-id clone-type compartment-id cpu-core-count data-storage-size-in-tbs db-name db-workload defined-tags display-name freeform-tags from-json help is-auto-scaling-enabled is-dedicated license-model max-wait-seconds source-id wait-for-state wait-interval-seconds'
        'db autonomous-database delete' = 'autonomous-database-id force from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-database generate-wallet' = 'autonomous-database-id file from-json help password'
        'db autonomous-database get' = 'autonomous-database-id from-json help'
        'db autonomous-database list' = 'all autonomous-container-database-id compartment-id db-workload display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db autonomous-database restore' = 'autonomous-database-id database-scn from-json help if-match latest max-wait-seconds timestamp wait-for-state wait-interval-seconds'
        'db autonomous-database start' = 'autonomous-database-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-database stop' = 'autonomous-database-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-database update' = 'admin-password autonomous-database-id cpu-core-count data-storage-size-in-tbs db-name defined-tags display-name force freeform-tags from-json help if-match is-auto-scaling-enabled license-model max-wait-seconds wait-for-state wait-interval-seconds whitelisted-ips'
        'db autonomous-database-backup create' = 'autonomous-database-id display-name from-json help max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-database-backup get' = 'autonomous-database-backup-id from-json help'
        'db autonomous-database-backup list' = 'all autonomous-database-id compartment-id display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db autonomous-exadata-infrastructure get' = 'autonomous-exadata-infrastructure-id from-json help'
        'db autonomous-exadata-infrastructure launch' = 'availability-domain compartment-id defined-tags display-name domain freeform-tags from-json help license-model maintenance-window-details max-wait-seconds shape subnet-id wait-for-state wait-interval-seconds'
        'db autonomous-exadata-infrastructure list' = 'all availability-domain compartment-id display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db autonomous-exadata-infrastructure terminate' = 'autonomous-exadata-infrastructure-id force from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-exadata-infrastructure update' = 'autonomous-exadata-infrastructure-id defined-tags display-name force freeform-tags from-json help if-match maintenance-window-details max-wait-seconds wait-for-state wait-interval-seconds'
        'db autonomous-exadata-infrastructure-shape list' = 'all availability-domain compartment-id from-json help limit page page-size'
        'db backup create' = 'database-id display-name from-json help max-wait-seconds wait-for-state wait-interval-seconds'
        'db backup delete' = 'backup-id force from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db backup get' = 'backup-id from-json help'
        'db backup list' = 'all compartment-id database-id from-json help limit page page-size'
        'db data-guard-association create from-existing-db-system' = 'creation-type database-admin-password database-id from-json help peer-db-system-id protection-mode transport-type'
        'db data-guard-association create with-new-db-system' = 'availability-domain creation-type database-admin-password database-id display-name from-json help hostname protection-mode subnet-id transport-type'
        'db data-guard-association failover' = 'data-guard-association-id database-admin-password database-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db data-guard-association get' = 'data-guard-association-id database-id from-json help'
        'db data-guard-association list' = 'all database-id from-json help limit page page-size'
        'db data-guard-association reinstate' = 'data-guard-association-id database-admin-password database-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db data-guard-association switchover' = 'data-guard-association-id database-admin-password database-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db database create' = 'admin-password auto-backup-enabled character-set db-name db-system-id db-version db-workload from-json help max-wait-seconds ncharacter-set pdb-name recovery-window-in-days source wait-for-state wait-interval-seconds'
        'db database create-from-backup' = 'admin-password backup-id backup-tde-password db-name db-system-id from-json help max-wait-seconds wait-for-state wait-interval-seconds'
        'db database delete' = 'database-id force from-json help'
        'db database get' = 'database-id from-json help'
        'db database list' = 'compartment-id db-system-id display-name from-json help lifecycle-state limit sort-by sort-order'
        'db database patch' = 'database-id from-json help patch-action patch-id'
        'db database restore' = 'database-id database-scn from-json help if-match latest max-wait-seconds timestamp wait-for-state wait-interval-seconds'
        'db database update' = 'auto-backup-enabled database-id defined-tags force freeform-tags from-json help if-match max-wait-seconds recovery-window-in-days wait-for-state wait-interval-seconds'
        'db external-backup-job complete' = 'backup-id cf-backup-handle data-size from-json help if-match redo-size spf-backup-handle sql-patches tde-wallet-path'
        'db external-backup-job create' = 'availability-domain character-set compartment-id database-edition database-mode db-name db-unique-name db-version display-name external-database-identifier from-json help ncharacter-set pdb-name'
        'db external-backup-job get' = 'backup-id from-json help'
        'db maintenance-run get' = 'from-json help maintenance-run-id'
        'db maintenance-run list' = 'all availability-domain compartment-id from-json help lifecycle-state limit maintenance-type page page-size sort-by sort-order target-resource-id target-resource-type'
        'db maintenance-run update' = 'from-json help if-match is-enabled maintenance-run-id max-wait-seconds wait-for-state wait-interval-seconds'
        'db node get' = 'db-node-id from-json help'
        'db node list' = 'all compartment-id db-system-id from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db node reset' = 'db-node-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db node soft-reset' = 'db-node-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db node start' = 'db-node-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db node stop' = 'db-node-id from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db patch get by-database' = 'database-id from-json help patch-id'
        'db patch get by-db-system' = 'db-system-id from-json help patch-id'
        'db patch list by-database' = 'all database-id from-json help limit page page-size'
        'db patch list by-db-system' = 'all db-system-id from-json help limit page page-size'
        'db patch-history get by-database' = 'database-id from-json help patch-history-entry-id'
        'db patch-history get by-db-system' = 'db-system-id from-json help patch-history-entry-id'
        'db patch-history list by-database' = 'all database-id from-json help limit page page-size'
        'db patch-history list by-db-system' = 'all db-system-id from-json help limit page page-size'
        'db system get' = 'db-system-id from-json help'
        'db system get-exadata-iorm-config' = 'db-system-id from-json help'
        'db system launch' = 'admin-password auto-backup-enabled availability-domain backup-subnet-id character-set cluster-name compartment-id cpu-core-count data-storage-percentage database-edition db-name db-version db-workload defined-tags disk-redundancy display-name domain fault-domains freeform-tags from-json help hostname initial-data-storage-size-in-gb license-model max-wait-seconds ncharacter-set node-count pdb-name recovery-window-in-days shape sparse-diskgroup ssh-authorized-keys-file subnet-id time-zone wait-for-state wait-interval-seconds'
        'db system launch-from-backup' = 'admin-password availability-domain backup-id backup-subnet-id backup-tde-password cluster-name compartment-id cpu-core-count data-storage-percentage database-edition db-name defined-tags disk-redundancy display-name domain fault-domains freeform-tags from-json help hostname initial-data-storage-size-in-gb license-model max-wait-seconds node-count shape sparse-diskgroup ssh-authorized-keys-file subnet-id time-zone wait-for-state wait-interval-seconds'
        'db system list' = 'all availability-domain backup-id compartment-id display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'db system patch' = 'db-system-id from-json help patch-action patch-id'
        'db system terminate' = 'db-system-id force from-json help if-match max-wait-seconds wait-for-state wait-interval-seconds'
        'db system update' = 'cpu-core-count data-storage-size-in-gbs db-system-id defined-tags force freeform-tags from-json help if-match max-wait-seconds patch-action patch-id ssh-authorized-keys-file wait-for-state wait-interval-seconds'
        'db system update-exadata-iorm-config' = 'db-plans db-system-id force from-json help if-match max-wait-seconds objective wait-for-state wait-interval-seconds'
        'db system-shape list' = 'all availability-domain compartment-id from-json help limit page page-size'
        'db version list' = 'all compartment-id db-system-id db-system-shape from-json help limit page page-size'
    }
    return $ociCommandsToLongParams
}

function GetOciCommandsToShortParams_db() {
    $ociCommandsToShortParams = @{
        'db autonomous-container-database create' = '? c h'
        'db autonomous-container-database get' = '? h'
        'db autonomous-container-database list' = '? c h'
        'db autonomous-container-database restart' = '? h'
        'db autonomous-container-database terminate' = '? h'
        'db autonomous-container-database update' = '? h'
        'db autonomous-data-warehouse create' = '? c h'
        'db autonomous-data-warehouse delete' = '? h'
        'db autonomous-data-warehouse generate-wallet' = '? h'
        'db autonomous-data-warehouse get' = '? h'
        'db autonomous-data-warehouse list' = '? c h'
        'db autonomous-data-warehouse restore' = '? h'
        'db autonomous-data-warehouse start' = '? h'
        'db autonomous-data-warehouse stop' = '? h'
        'db autonomous-data-warehouse update' = '? h'
        'db autonomous-data-warehouse-backup create' = '? h'
        'db autonomous-data-warehouse-backup get' = '? h'
        'db autonomous-data-warehouse-backup list' = '? c h'
        'db autonomous-database create' = '? c h'
        'db autonomous-database create-from-clone' = '? c h'
        'db autonomous-database delete' = '? h'
        'db autonomous-database generate-wallet' = '? h'
        'db autonomous-database get' = '? h'
        'db autonomous-database list' = '? c h'
        'db autonomous-database restore' = '? h'
        'db autonomous-database start' = '? h'
        'db autonomous-database stop' = '? h'
        'db autonomous-database update' = '? h'
        'db autonomous-database-backup create' = '? h'
        'db autonomous-database-backup get' = '? h'
        'db autonomous-database-backup list' = '? c h'
        'db autonomous-exadata-infrastructure get' = '? h'
        'db autonomous-exadata-infrastructure launch' = '? c h'
        'db autonomous-exadata-infrastructure list' = '? c h'
        'db autonomous-exadata-infrastructure terminate' = '? h'
        'db autonomous-exadata-infrastructure update' = '? h'
        'db autonomous-exadata-infrastructure-shape list' = '? c h'
        'db backup create' = '? h'
        'db backup delete' = '? h'
        'db backup get' = '? h'
        'db backup list' = '? c h'
        'db data-guard-association create from-existing-db-system' = '? h'
        'db data-guard-association create with-new-db-system' = '? h'
        'db data-guard-association failover' = '? h'
        'db data-guard-association get' = '? h'
        'db data-guard-association list' = '? h'
        'db data-guard-association reinstate' = '? h'
        'db data-guard-association switchover' = '? h'
        'db database create' = '? h'
        'db database create-from-backup' = '? h'
        'db database delete' = '? h'
        'db database get' = '? h'
        'db database list' = '? c h'
        'db database patch' = '? h'
        'db database restore' = '? h'
        'db database update' = '? h'
        'db external-backup-job complete' = '? h'
        'db external-backup-job create' = '? c h'
        'db external-backup-job get' = '? h'
        'db maintenance-run get' = '? h'
        'db maintenance-run list' = '? c h'
        'db maintenance-run update' = '? h'
        'db node get' = '? h'
        'db node list' = '? c h'
        'db node reset' = '? h'
        'db node soft-reset' = '? h'
        'db node start' = '? h'
        'db node stop' = '? h'
        'db patch get by-database' = '? h'
        'db patch get by-db-system' = '? h'
        'db patch list by-database' = '? h'
        'db patch list by-db-system' = '? h'
        'db patch-history get by-database' = '? h'
        'db patch-history get by-db-system' = '? h'
        'db patch-history list by-database' = '? h'
        'db patch-history list by-db-system' = '? h'
        'db system get' = '? h'
        'db system get-exadata-iorm-config' = '? h'
        'db system launch' = '? c h'
        'db system launch-from-backup' = '? c h'
        'db system list' = '? c h'
        'db system patch' = '? h'
        'db system terminate' = '? h'
        'db system update' = '? h'
        'db system update-exadata-iorm-config' = '? h'
        'db system-shape list' = '? c h'
        'db version list' = '? c h'
    }
    return $ociCommandsToShortParams
}