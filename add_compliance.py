import re

with open('/Users/user/Downloads/SNS-Groups/mandatory-disclosure/index.html', 'r') as f:
    content = f.read()

# We need to insert a Compliance section after every "B. Documents and Information" table container's enclosing div.

compliance_template = """
        <div class="scroll-animate visible mt-12">
          <h3 class="disc-section-title" style="border-left-color: #f59e0b;">C. Compliance</h3>
          <div class="disc-table-container">
            <table class="disc-table">
              <thead>
                <tr>
                  <th class="w-24" style="background:#f59e0b;">SL NO.</th>
                  <th style="background:#f59e0b;">COMPLIANCE DOCUMENTS/INFORMATION</th>
                  <th style="background:#f59e0b;">LINKS</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>COMPLIANCE DOCUMENT EXAMPLE</td>
                  <td><a href="#" target="_blank" class="disc-link" style="color:#d97706;"><i class="fas fa-file-pdf"></i> View Document</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>"""

k12_compliance_template = """
        <div class="scroll-animate visible mt-12">
          <h3 class="text-2xl font-bold mb-6 text-gray-800 border-l-4 border-amber-500 pl-4 uppercase">C. Compliance</h3>
          <div class="overflow-x-auto rounded-2xl border border-amber-200 shadow-lg bg-white">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-amber-500 text-white">
                  <th class="px-6 py-4 text-xs font-bold border-b border-amber-200 w-24 uppercase">SL NO.</th>
                  <th class="px-6 py-4 text-xs font-bold border-b border-amber-200 uppercase">COMPLIANCE DOCUMENTS/INFORMATION</th>
                  <th class="px-6 py-4 text-xs font-bold border-b border-amber-200 uppercase">LINKS</th>
                </tr>
              </thead>
              <tbody>
                <tr class="hover:bg-amber-50/30 transition-colors bg-white">
                  <td class="px-6 py-4 text-sm text-gray-700 border-b border-gray-100 font-medium">1</td>
                  <td class="px-6 py-4 text-sm text-gray-700 border-b border-gray-100 uppercase font-medium">Compliance Document Example</td>
                  <td class="px-6 py-4 text-sm border-b border-gray-100"><a href="#" class="text-amber-700 font-bold uppercase inline-flex items-center gap-2"><i class="fas fa-file-pdf"></i> View Document</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>"""

# For K-12
target_k12 = """                  <td class="px-6 py-4 text-sm border-b border-gray-100"><a href="#"
                      class="text-blue-800 font-bold uppercase inline-flex items-center gap-2"><i
                        class="fas fa-file-pdf"></i> View Document</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>"""
content = content.replace(target_k12, target_k12 + k12_compliance_template, 1)

# For Engineering & Tech
target_eng = """                  <td><a href="Tech/Strategy Plan.pdf" target="_blank" class="disc-link"><i class="fas fa-file-pdf"></i>
                      View Document</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>"""
content = content.replace(target_eng, target_eng + compliance_template, 1)

# For Arts & Science
target_arts = """                  <td><a href="Arts-Science/Mandatory Disclosure Document.pdf" target="_blank" class="disc-link"><i
                        class="fas fa-file-pdf"></i> View Document</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>"""
content = content.replace(target_arts, target_arts + compliance_template, 1)

# For Paramedical Pharmacy
target_pharm = """            <tr><td>2</td><td>Copy of Valid Fire Safety Certificate</td><td><a href="https://snscphs.org/mandatory-disclosure/" target="_blank" class="disc-link"><i class="fas fa-file-pdf"></i> View Document</a></td></tr>
          </tbody></table></div>
        </div>"""
content = content.replace(target_pharm, target_pharm.replace('</div>', '') + compliance_template + '\n        </div>', 1)

# For Paramedical Nursing
target_nurs = """            <tr><td>8</td><td>TNMGRMU Certificate of Registration (COR)</td><td><a href="https://snscnursing.org/pages/mandatory-disclosure.html" target="_blank" class="disc-link"><i class="fas fa-file-pdf"></i> View Document</a></td></tr>
          </tbody></table></div>
        </div>"""
content = content.replace(target_nurs, target_nurs.replace('</div>', '') + compliance_template + '\n        </div>', 1)

# For Paramedical Allied
target_allied = """            <tr><td>5</td><td>Copies of Valid Water, Health and Sanitation Certificates</td><td><a href="https://snscahs.org/pages/mandatory-disclosure.html" target="_blank" class="disc-link"><i class="fas fa-file-pdf"></i> View Document</a></td></tr>
          </tbody></table></div>
        </div>"""
content = content.replace(target_allied, target_allied.replace('</div>', '') + compliance_template + '\n        </div>', 1)

# For Paramedical Physio
target_physio = """            <tr><td>6</td><td>Copy of Health and Family Welfare</td><td><a href="https://snscphysio.org/mandatory-disclosure/" target="_blank" class="disc-link"><i class="fas fa-file-pdf"></i> View Document</a></td></tr>
          </tbody></table></div>
        </div>"""
content = content.replace(target_physio, target_physio.replace('</div>', '') + compliance_template + '\n        </div>', 1)

# For Education
target_edu = """            <tr><td>9</td><td>Copy of Sanitary Certificate</td><td><a href="https://drsnsce.edu.in/mandatory-disclosure/" target="_blank" class="disc-link"><i class="fas fa-file-pdf"></i> View Document</a></td></tr>
          </tbody></table></div>
        </div>"""
content = content.replace(target_edu, target_edu.replace('</div>', '') + compliance_template + '\n        </div>', 1)

with open('/Users/user/Downloads/SNS-Groups/mandatory-disclosure/index.html', 'w') as f:
    f.write(content)

print("Done")
