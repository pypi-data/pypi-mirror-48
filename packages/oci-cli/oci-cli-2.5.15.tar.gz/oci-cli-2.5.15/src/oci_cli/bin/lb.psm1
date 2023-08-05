function GetOciTopLevelCommand_lb() {
    return 'lb'
}

function GetOciSubcommands_lb() {
    $ociSubcommands = @{
        'lb' = 'backend backend-health backend-set backend-set-health certificate health-checker hostname listener load-balancer load-balancer-health path-route-set policy protocol rule-set shape work-request'
        'lb backend' = 'create delete get list update'
        'lb backend-health' = 'get'
        'lb backend-set' = 'create delete get list update'
        'lb backend-set-health' = 'get'
        'lb certificate' = 'create delete list'
        'lb health-checker' = 'get update'
        'lb hostname' = 'create delete get list update'
        'lb listener' = 'create delete update'
        'lb load-balancer' = 'create delete get list update'
        'lb load-balancer-health' = 'get list'
        'lb path-route-set' = 'create delete get list update'
        'lb policy' = 'list'
        'lb protocol' = 'list'
        'lb rule-set' = 'create delete get list update'
        'lb shape' = 'list'
        'lb work-request' = 'get list'
    }
    return $ociSubcommands
}

function GetOciCommandsToLongParams_lb() {
    $ociCommandsToLongParams = @{
        'lb backend create' = 'backend-set-name backup drain from-json help ip-address load-balancer-id max-wait-seconds offline port wait-for-state wait-interval-seconds weight'
        'lb backend delete' = 'backend-name backend-set-name force from-json help load-balancer-id max-wait-seconds wait-for-state wait-interval-seconds'
        'lb backend get' = 'backend-name backend-set-name from-json help load-balancer-id'
        'lb backend list' = 'all backend-set-name from-json help load-balancer-id'
        'lb backend update' = 'backend-name backend-set-name backup drain from-json help load-balancer-id max-wait-seconds offline wait-for-state wait-interval-seconds weight'
        'lb backend-health get' = 'backend-name backend-set-name from-json help load-balancer-id'
        'lb backend-set create' = 'backends from-json health-checker-interval-in-ms health-checker-port health-checker-protocol health-checker-response-body-regex health-checker-retries health-checker-return-code health-checker-timeout-in-ms health-checker-url-path help load-balancer-id max-wait-seconds name policy session-persistence-cookie-name session-persistence-disable-fallback ssl-certificate-name ssl-verify-depth ssl-verify-peer-certificate wait-for-state wait-interval-seconds'
        'lb backend-set delete' = 'backend-set-name force from-json help load-balancer-id max-wait-seconds wait-for-state wait-interval-seconds'
        'lb backend-set get' = 'backend-set-name from-json help load-balancer-id'
        'lb backend-set list' = 'all from-json help load-balancer-id'
        'lb backend-set update' = 'backend-set-name backends force from-json health-checker-interval-in-ms health-checker-port health-checker-protocol health-checker-response-body-regex health-checker-retries health-checker-return-code health-checker-timeout-in-ms health-checker-url-path help load-balancer-id max-wait-seconds policy session-persistence-cookie-name session-persistence-disable-fallback ssl-certificate-name ssl-verify-depth ssl-verify-peer-certificate wait-for-state wait-interval-seconds'
        'lb backend-set-health get' = 'backend-set-name from-json help load-balancer-id'
        'lb certificate create' = 'ca-certificate-file certificate-name from-json help load-balancer-id max-wait-seconds passphrase private-key-file public-certificate-file wait-for-state wait-interval-seconds'
        'lb certificate delete' = 'certificate-name force from-json help load-balancer-id max-wait-seconds wait-for-state wait-interval-seconds'
        'lb certificate list' = 'all from-json help load-balancer-id'
        'lb health-checker get' = 'backend-set-name from-json help load-balancer-id'
        'lb health-checker update' = 'backend-set-name from-json help interval-in-millis load-balancer-id max-wait-seconds port protocol response-body-regex retries return-code timeout-in-millis url-path wait-for-state wait-interval-seconds'
        'lb hostname create' = 'from-json help hostname load-balancer-id max-wait-seconds name wait-for-state wait-interval-seconds'
        'lb hostname delete' = 'force from-json help load-balancer-id max-wait-seconds name wait-for-state wait-interval-seconds'
        'lb hostname get' = 'from-json help load-balancer-id name'
        'lb hostname list' = 'all from-json help load-balancer-id'
        'lb hostname update' = 'from-json help hostname load-balancer-id max-wait-seconds name wait-for-state wait-interval-seconds'
        'lb listener create' = 'connection-configuration-idle-timeout default-backend-set-name from-json help hostname-names load-balancer-id max-wait-seconds name path-route-set-name port protocol rule-set-names ssl-certificate-name ssl-verify-depth ssl-verify-peer-certificate wait-for-state wait-interval-seconds'
        'lb listener delete' = 'force from-json help listener-name load-balancer-id max-wait-seconds wait-for-state wait-interval-seconds'
        'lb listener update' = 'connection-configuration-idle-timeout default-backend-set-name force from-json help hostname-names listener-name load-balancer-id max-wait-seconds path-route-set-name port protocol rule-set-names ssl-certificate-name ssl-verify-depth ssl-verify-peer-certificate wait-for-state wait-interval-seconds'
        'lb load-balancer create' = 'backend-sets certificates compartment-id defined-tags display-name freeform-tags from-json help hostnames is-private listeners max-wait-seconds path-route-sets rule-sets shape-name subnet-ids wait-for-state wait-interval-seconds'
        'lb load-balancer delete' = 'force from-json help load-balancer-id max-wait-seconds wait-for-state wait-interval-seconds'
        'lb load-balancer get' = 'from-json help load-balancer-id'
        'lb load-balancer list' = 'all compartment-id detail display-name from-json help lifecycle-state limit page page-size sort-by sort-order'
        'lb load-balancer update' = 'defined-tags display-name force freeform-tags from-json help load-balancer-id max-wait-seconds wait-for-state wait-interval-seconds'
        'lb load-balancer-health get' = 'from-json help load-balancer-id'
        'lb load-balancer-health list' = 'all compartment-id from-json help limit page page-size'
        'lb path-route-set create' = 'from-json help load-balancer-id max-wait-seconds name path-routes wait-for-state wait-interval-seconds'
        'lb path-route-set delete' = 'force from-json help load-balancer-id max-wait-seconds path-route-set-name wait-for-state wait-interval-seconds'
        'lb path-route-set get' = 'from-json help load-balancer-id path-route-set-name'
        'lb path-route-set list' = 'all from-json help load-balancer-id'
        'lb path-route-set update' = 'force from-json help load-balancer-id max-wait-seconds path-route-set-name path-routes wait-for-state wait-interval-seconds'
        'lb policy list' = 'all compartment-id from-json help limit page page-size'
        'lb protocol list' = 'all compartment-id from-json help limit page page-size'
        'lb rule-set create' = 'from-json help items load-balancer-id max-wait-seconds name wait-for-state wait-interval-seconds'
        'lb rule-set delete' = 'force from-json help load-balancer-id max-wait-seconds rule-set-name wait-for-state wait-interval-seconds'
        'lb rule-set get' = 'from-json help load-balancer-id rule-set-name'
        'lb rule-set list' = 'all from-json help load-balancer-id'
        'lb rule-set update' = 'force from-json help items load-balancer-id max-wait-seconds rule-set-name wait-for-state wait-interval-seconds'
        'lb shape list' = 'all compartment-id from-json help limit page page-size'
        'lb work-request get' = 'from-json help work-request-id'
        'lb work-request list' = 'all from-json help limit load-balancer-id page page-size'
    }
    return $ociCommandsToLongParams
}

function GetOciCommandsToShortParams_lb() {
    $ociCommandsToShortParams = @{
        'lb backend create' = '? h'
        'lb backend delete' = '? h'
        'lb backend get' = '? h'
        'lb backend list' = '? h'
        'lb backend update' = '? h'
        'lb backend-health get' = '? h'
        'lb backend-set create' = '? h'
        'lb backend-set delete' = '? h'
        'lb backend-set get' = '? h'
        'lb backend-set list' = '? h'
        'lb backend-set update' = '? h'
        'lb backend-set-health get' = '? h'
        'lb certificate create' = '? h'
        'lb certificate delete' = '? h'
        'lb certificate list' = '? h'
        'lb health-checker get' = '? h'
        'lb health-checker update' = '? h'
        'lb hostname create' = '? h'
        'lb hostname delete' = '? h'
        'lb hostname get' = '? h'
        'lb hostname list' = '? h'
        'lb hostname update' = '? h'
        'lb listener create' = '? h'
        'lb listener delete' = '? h'
        'lb listener update' = '? h'
        'lb load-balancer create' = '? c h'
        'lb load-balancer delete' = '? h'
        'lb load-balancer get' = '? h'
        'lb load-balancer list' = '? c h'
        'lb load-balancer update' = '? h'
        'lb load-balancer-health get' = '? h'
        'lb load-balancer-health list' = '? c h'
        'lb path-route-set create' = '? h'
        'lb path-route-set delete' = '? h'
        'lb path-route-set get' = '? h'
        'lb path-route-set list' = '? h'
        'lb path-route-set update' = '? h'
        'lb policy list' = '? c h'
        'lb protocol list' = '? c h'
        'lb rule-set create' = '? h'
        'lb rule-set delete' = '? h'
        'lb rule-set get' = '? h'
        'lb rule-set list' = '? h'
        'lb rule-set update' = '? h'
        'lb shape list' = '? c h'
        'lb work-request get' = '? h'
        'lb work-request list' = '? h'
    }
    return $ociCommandsToShortParams
}