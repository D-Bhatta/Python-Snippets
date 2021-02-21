# Security Recommendation Checklist

## Checklist

- [ ] **When you build custom VM images, apply the latest updates.**
  - *Before you create images, install the latest updates for the operating system and for all applications that will be part of your image.*
- [ ] **Keep your VMs current.**
  - *You can use the  Update Management solution in Azure Automation to manage operating system updates for your Windows and Linux computers in Azure.*
- [ ] **Back up your VMs.**
  - *Azure Backup helps protect your application data and has minimal operating costs. Application errors can corrupt your data, and human errors can introduce bugs into your applications. Azure Backup protects your VMs that run Windows and Linux.*
- [ ] **Use multiple VMs for greater resilience and availability.**
  - *If your VM runs applications that must be highly available, use multiple VMs or availability sets.*
- [ ] **Adopt a business continuity and disaster recovery (BCDR) strategy.**
  - *Azure Site Recovery allows you to choose from different options designed to support business continuity. It supports different replication and failover scenarios. For more information, see About Site Recovery.*
- [ ] **Encrypt operating system disks.**
  - *Azure Disk Encryption helps you encrypt your Windows and Linux IaaS VM disks. Without the necessary keys, the contents of encrypted disks are unreadable. Disk encryption protects stored data from unauthorized access that would otherwise be possible if the disk were copied.*
- [ ] **Encrypt data disks.**
  - *Azure Disk Encryption*
- [ ] **Limit installed software.**
  - *Limit installed software to what is required to successfully apply your solution. This guideline helps reduce your solution's attack surface.*
- [ ] **Use antivirus or antimalware.**
  - *In Azure, you can use antimalware software from security vendors such as Microsoft, Symantec, Trend Micro, and Kaspersky. This software helps protect your VMs from malicious files, adware, and other threats. You can deploy Microsoft Antimalware based on your application workloads. Microsoft Antimalware is available for Windows machines only. Use either basic secure-by-default or advanced custom configuration. For more information, see  Microsoft Antimalware for Azure Cloud Services and Virtual Machines.*
- [ ] **Securely store keys and secrets.**
  - *Simplify the management of your secrets and keys by providing your application owners with a secure, centrally managed option. This management reduces the risk of an accidental compromise or leak. Azure Key Vault can securely store your keys in hardware security modules (HSMs) that are certified to FIPS 140-2 Level 2. If you need to use FIPs 140.2 Level 3 to store your keys and secrets, you can use Azure Dedicated HSM.*
- [ ] **Centralize VM authentication.**
  - *You can centralize the authentication of your Windows and Linux VMs by using  Azure Active Directory authentication.*
- [ ] **Monitor your VMs.**
  - *You can use Azure Monitor for VMs to monitor the state of your Azure VMs and virtual machine scale sets. Performance issues with a VM can lead to service disruption, which violates the security principle of availability.*
- [ ] **Restrict access to management ports.**
  - *Attackers scan public cloud IP ranges for open management ports and attempt "easy" attacks like common passwords and known unpatched vulnerabilities. You can use  just-in-time (JIT) VM access to lock down inbound traffic to your Azure VMs, reducing exposure to attacks while providing easy connections to VMs when they're needed.*
- [ ] **Limit network access.**
  - *Network security groups allow you to restrict network access and control the number of exposed endpoints. For more information, see Create, change, or delete a network security group.*
